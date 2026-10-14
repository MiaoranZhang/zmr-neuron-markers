"""Download pinned data for LOCAL review; never execute upstream code."""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import ssl
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 25 * 1024 * 1024


def fetch(url):
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.hostname not in {'codeload.github.com', 'raw.githubusercontent.com'}:
        raise ValueError('Only registered public HTTPS data hosts are permitted')
    request = Request(url, headers={'User-Agent': 'zmr-neuron-markers/1.0'})
    with urlopen(request, timeout=45, context=ssl.create_default_context()) as response:
        result = response.read(MAX_BYTES + 1)
    if len(result) > MAX_BYTES:
        raise ValueError('Data exceeded the small-source download limit')
    return result


def parse_siletti(archive):
    """Keep path identities and author rule semantics, including duplicate names."""
    panels, assertions, licenses = [], [], []
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        total_size = sum(i.file_size for i in z.infolist())
        if total_size > MAX_BYTES:
            raise ValueError('Uncompressed source exceeded the size limit')
        for info in z.infolist():
            relative = '/'.join(info.filename.split('/')[1:])
            if relative.upper().endswith(('LICENSE', 'LICENSE.TXT', 'LICENSE.MD', 'COPYING')):
                licenses.append(relative)
            if not relative.startswith(('Human_adult/', 'Neuropeptides/')) or not relative.endswith('.md'):
                continue
            text = z.read(info).decode('utf-8-sig')
            def field(key):
                found = re.search(rf'^{key}:\s*([^\r\n]*)', text, re.M)
                return found.group(1).strip() if found else ''
            definition = field('definition')
            tokens = re.findall(r'([+-])([A-Za-z0-9_.-]+)', definition)
            if not tokens:
                raise ValueError(f'Unparsed definition in {relative}')
            remainder = re.sub(r'[+-][A-Za-z0-9_.-]+', '', definition).strip()
            if remainder:
                raise ValueError(f'Unknown rule syntax in {relative}: {remainder}')
            if relative.startswith('Neuropeptides/'):
                category = 'neuropeptide_program'
            elif '/Neurotransmission/' in relative:
                category = 'transmitter'
            elif '/State/' in relative:
                category = 'state_program'
            elif '/Subtype/' in relative:
                category = 'source_regional_subtype'
            else:
                category = 'source_lineage'
            panel_id = 'siletti:' + relative
            panels.append(dict(panel_id=panel_id, name=field('name'), abbreviation=field('abbreviation'),
                               source_category_raw=field('categories'), review_category=category,
                               source_definition=definition, source_locator=relative,
                               source_sha256=hashlib.sha256(z.read(info)).hexdigest(),
                               species='human_atlas; upstream_evidence_may_include_mouse', stage='adult_atlas',
                               region='source_specific; review before transfer'))
            for polarity, gene in tokens:
                assertions.append(dict(panel_id=panel_id, source_id='siletti_rules',
                                       gene_symbol_raw=gene,
                                       polarity='source_positive' if polarity == '+' else 'source_negative',
                                       source_locator=relative))
    return panels, assertions, licenses


def parse_sctype(workbook):
    try:
        import pandas as pd
    except ImportError as error:
        raise RuntimeError('ScType Excel import requires existing pandas/openpyxl; no installation attempted') from error
    data = pd.read_excel(io.BytesIO(workbook))
    required = {'tissueType', 'cellName', 'geneSymbolmore1', 'geneSymbolmore2'}
    if not required.issubset(data.columns):
        raise ValueError('ScType workbook schema changed')
    panels, assertions = [], []
    for index, row in data.loc[data.tissueType.eq('Brain')].iterrows():
        panel_id = f'sctype:Brain:{index + 2}:{row.cellName}'
        locator = f'ScTypeDB_full.xlsx; Excel row {index + 2}; Brain/{row.cellName}'
        negative_missing = pd.isna(row.geneSymbolmore2) or not str(row.geneSymbolmore2).strip()
        panels.append(dict(panel_id=panel_id, name=str(row.cellName), source_locator=locator,
                           species='unspecified', stage='unspecified', region='Brain_unspecified',
                           negative_status='not_provided' if negative_missing else 'source_provided'))
        for field, polarity in [('geneSymbolmore1', 'source_positive'), ('geneSymbolmore2', 'source_negative')]:
            value = row[field]
            if pd.isna(value):
                continue
            for gene in str(value).split(','):
                gene = gene.strip()
                if gene:
                    assertions.append(dict(panel_id=panel_id, source_id='sctype', gene_symbol_raw=gene,
                                           polarity=polarity, source_locator=locator))
    return panels, assertions


def write_tsv(path, rows):
    if not rows:
        raise ValueError('Empty source output')
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, choices=['siletti_rules', 'sctype'])
    parser.add_argument('--out', type=Path, default=ROOT / 'local_imports')
    args = parser.parse_args()
    target = args.out.resolve() / args.source
    for public_folder in ['assets', 'references', 'scripts', 'agents', 'tests']:
        if target.is_relative_to(ROOT / public_folder):
            raise ValueError('Local upstream imports cannot be written into public package folders')
    if target.exists():
        raise FileExistsError('Source folder exists; choose a new versioned cache, no overwrite performed')
    registry = json.loads((ROOT / 'assets/source_registry.json').read_text(encoding='utf-8'))
    source = next(s for s in registry['sources'] if s['source_id'] == args.source)
    if args.source == 'siletti_rules':
        url = source['archive_url']
        payload = fetch(url)
        panels, assertions, licenses = parse_siletti(payload)
        payload_name = 'source_archive.zip'
        license_payload = None
    else:
        url = source['download_url']
        payload = fetch(url)
        panels, assertions = parse_sctype(payload)
        payload_name = 'ScTypeDB_full.xlsx'
        license_url = f"https://raw.githubusercontent.com/{source['repository']}/{source['version']}/LICENSE"
        license_payload = fetch(license_url)
        licenses = ['LICENSE']
    if not panels or len({p['panel_id'] for p in panels}) != len(panels):
        raise ValueError('Empty or duplicate source panel IDs')
    target.mkdir(parents=True)
    (target / payload_name).write_bytes(payload)
    if license_payload is not None:
        (target / 'LICENSE').write_bytes(license_payload)
    write_tsv(target / 'panels.tsv', panels)
    write_tsv(target / 'marker_assertions.tsv', assertions)
    manifest = dict(source_id=args.source, version=source['version'], source_url=url,
                    retrieval_utc=datetime.now(timezone.utc).isoformat(),
                    sha256=hashlib.sha256(payload).hexdigest(), n_panels=len(panels),
                    n_assertions=len(assertions), license_files_found=licenses,
                    license_status=source['license_status'], publication_status='LOCAL_REVIEW_ONLY',
                    upstream_code_executed=False)
    (target / 'import_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
