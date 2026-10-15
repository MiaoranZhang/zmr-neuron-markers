"""Build the small independently curated fact index against local pinned sources."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
MANUAL_FACTS = {
    ('wang_2024', 'Neuron auxiliary NRGN'): (['NRGN'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/', 'Methods: Cluster cell-type annotation; neuronal auxiliary evidence only'),
    ('wang_2024', 'RIT2 neuronal program'): (['RIT2'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/', 'Fig1C/Fig2/TableS2 C9; not a fixed type or mandatory GALNTL6 combination'),
    ('wang_2024', 'GALNTL6 neuronal program'): (['GALNTL6'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/', 'Fig1C/Fig4/TableS2 C6 and subclusters; separate expression program'),
    ('panglaodb', 'Neurons'): (['SNAP25', 'STMN2'], 'https://panglaodb.se/markers.html?cell_type=%27Neurons%27', 'Selected Neurons rows inspected 2026-10-14; species column Mm Hs; no specificity validation'),
    ('kamath_2022', 'DA core triad'): (['TH', 'SLC6A3', 'SLC18A2'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/', 'Results: A molecular taxonomy of human SNpc DA neurons; Extended Data Fig1i,j'),
    ('kamath_2022', 'SOX6 DA branch'): (['SOX6'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/', 'Fig1e and Results: SOX6/CALB1 DA branches'),
    ('kamath_2022', 'CALB1 DA branch'): (['CALB1'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/', 'Fig1e and Results: SOX6/CALB1 DA branches'),
    ('kamath_2022', 'SOX6_AGTR1 DA subtype'): (['SOX6', 'AGTR1'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/', 'Results/Fig3: SOX6_AGTR1 DA subtype; not a query vulnerability claim'),
    ('kamath_2022', 'CALB1_TMEM200A DA subtype'): (['CALB1', 'TMEM200A'], 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/', 'Results/Fig3: CALB1_TMEM200A DA subtype')
}


def load_rows(path):
    with path.open(encoding='utf-8') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def build(imports):
    registry = {s['source_id']: s for s in json.loads((ROOT / 'assets/source_registry.json').read_text(encoding='utf-8'))['sources']}
    panels = json.loads((ROOT / 'assets/curated_panels.json').read_text(encoding='utf-8'))['panels']
    locations = json.loads((ROOT / 'assets/panel_source_map.json').read_text(encoding='utf-8'))
    source_rows = {}
    for sid in ['siletti_rules', 'sctype']:
        source_rows[sid] = load_rows(imports / sid / 'marker_assertions.tsv')
        manifest = json.loads((imports / sid / 'import_manifest.json').read_text(encoding='utf-8'))
        if manifest['version'] != registry[sid]['version']:
            raise ValueError('Local source version differs from registry')
    result = []
    for panel in panels:
        for role in ['positive', 'negative']:
            for gene in panel[role]:
                evidence = []
                for sid, locators in locations[panel['id']].items():
                    for locator in locators:
                        if sid in source_rows:
                            for raw in source_rows[sid]:
                                locator_matches = (raw['source_locator'] == locator if sid == 'siletti_rules' else raw['source_locator'].endswith('Brain/' + locator))
                                if raw['gene_symbol_raw'] != gene or not locator_matches:
                                    continue
                                url = (f"https://github.com/{registry[sid]['repository']}/blob/{registry[sid]['version']}/{quote(locator)}"
                                       if sid == 'siletti_rules' else registry[sid]['download_url'])
                                evidence.append((sid, raw['source_locator'], url, raw['polarity']))
                        elif (sid, locator) in MANUAL_FACTS:
                            genes, url, fact_locator = MANUAL_FACTS[sid, locator]
                            if gene in genes:
                                evidence.append((sid, fact_locator, url, 'source_positive_association'))
                if not evidence:
                    raise ValueError(f'No inspected source supports {panel["id"]}/{gene}; do not invent provenance')
                for sid, locator, url, source_role in sorted(set(evidence)):
                    result.append(dict(panel_id=panel['id'], panel_label=panel['label'], review_category=panel['category'],
                                       gene_symbol_raw=gene, curated_role=role, source_id=sid,
                                       source_polarity=source_role, source_locator=locator, source_url=url,
                                       source_version=registry[sid]['version'], evidence_family=registry[sid]['evidence_family'],
                                       query_species_scope=panel['species'], query_stage_scope=panel['stage'],
                                       regions=';'.join(panel['regions']), curation_type='original_review_panel_not_literal_author_rule',
                                       source_species_context=registry[sid]['species']))
    return panels, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--imports', type=Path, default=ROOT / 'local_imports')
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    output = ROOT / 'assets/curated_marker_assertions.tsv'
    if output.exists() and not args.refresh:
        raise FileExistsError('Catalog exists; use --refresh only for an intended catalog update')
    panels, rows = build(args.imports)
    with output.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    summary = dict(n_panels=len(panels), n_distinct_genes=len({r['gene_symbol_raw'] for r in rows}),
                   n_panel_gene_roles=len({(r['panel_id'], r['gene_symbol_raw'], r['curated_role']) for r in rows}),
                   n_source_trace_rows=len(rows), categories=dict(Counter(p['category'] for p in panels)),
                   complete_upstream_catalogs_bundled=False, expression_reference_downloaded=False,
                   curated_panel_validation='source_trace_validation_only_not_classifier_accuracy')
    (ROOT / 'assets/catalog_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
