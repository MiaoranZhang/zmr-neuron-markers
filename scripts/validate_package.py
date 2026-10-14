"""Validate catalog structure, provenance and local/public separation, offline."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    required = ['SKILL.md', 'agents/openai.yaml', 'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
                'assets/source_registry.json', 'assets/curated_panels.json', 'assets/panel_source_map.json',
                'assets/curated_marker_assertions.tsv', 'assets/source_conflicts.tsv', 'assets/catalog_summary.json',
                'references/resource-guide.md', 'references/data-contract.md', 'references/annotation-workflow.md',
                'scripts/import_resources.py', 'scripts/audit_coverage.py', 'scripts/build_catalog.py']
    for name in required:
        if not (root / name).is_file():
            raise ValueError('Missing required package file: ' + name)
    entry = (root / 'SKILL.md').read_text(encoding='utf-8')
    if not entry.startswith('---\nname: zmr-neuron-markers\n') or '[TODO' in entry:
        raise ValueError('Invalid skill entrypoint')
    for link in re.findall(r'\]\(([^)]+)\)', entry):
        if not link.startswith('https://') and not (root / link).exists():
            raise ValueError('Missing routed resource: ' + link)
    registry = json.loads((root / 'assets/source_registry.json').read_text(encoding='utf-8'))
    sources = {r['source_id']: r for r in registry['sources']}
    if len(sources) != len(registry['sources']):
        raise ValueError('Duplicate source IDs')
    panels = json.loads((root / 'assets/curated_panels.json').read_text(encoding='utf-8'))['panels']
    ids = {p['id'] for p in panels}
    if len(ids) != len(panels):
        raise ValueError('Duplicate panel IDs')
    locations = json.loads((root / 'assets/panel_source_map.json').read_text(encoding='utf-8'))
    if set(locations) != ids:
        raise ValueError('Panel/source map does not match catalog')
    roles = set()
    for panel in panels:
        if not panel['positive'] or not panel['notes'] or not panel['regions']:
            raise ValueError('Empty panel evidence or applicability')
        if set(panel['positive']) & set(panel['negative']):
            raise ValueError('Conflicting polarity within a curated panel')
        if set(panel['sources']) != set(locations[panel['id']]) or not set(panel['sources']) <= set(sources):
            raise ValueError('Unregistered or inconsistent source')
        for role in ['positive', 'negative']:
            if len(panel[role]) != len(set(panel[role])):
                raise ValueError('Duplicate genes within panel role')
            roles.update((panel['id'], gene, role) for gene in panel[role])
    with (root / 'assets/curated_marker_assertions.tsv').open(encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    if {(r['panel_id'], r['gene_symbol_raw'], r['curated_role']) for r in rows} != roles:
        raise ValueError('Missing or extra traced panel/gene roles')
    for row in rows:
        source = sources.get(row['source_id'])
        if not source or not row['source_locator'] or not row['source_url'].startswith('https://'):
            raise ValueError('Incomplete source trace')
        if row['evidence_family'] != source['evidence_family'] or row['source_version'] != source['version']:
            raise ValueError('Evidence family or version mismatch')
        if row['curation_type'] != 'original_review_panel_not_literal_author_rule':
            raise ValueError('Review panels misrepresented as literal source rules')
    summary = json.loads((root / 'assets/catalog_summary.json').read_text(encoding='utf-8'))
    expected = dict(n_panels=len(panels), n_distinct_genes=len({r['gene_symbol_raw'] for r in rows}),
                    n_panel_gene_roles=len(roles), n_source_trace_rows=len(rows),
                    categories=dict(Counter(p['category'] for p in panels)))
    for key, value in expected.items():
        if summary[key] != value:
            raise ValueError('Catalog summary mismatch: ' + key)
    if summary['complete_upstream_catalogs_bundled'] or summary['expression_reference_downloaded']:
        raise ValueError('Unsupported acquisition/completeness claim')
    return dict(status='PASS', **expected, biological_classifier_validated=False,
                note='Structural/source-trace validation; not held-out annotation accuracy')


if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
