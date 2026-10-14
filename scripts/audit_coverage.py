"""Audit measured gene symbols only; never infer cell identities or true negatives."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def audit(panels, genes, region, species):
    rows = []
    for panel in panels:
        positive, negative = set(panel['positive']), set(panel['negative'])
        region_status = 'review_required_unknown_region' if region == 'unknown' else (
            'context_matches' if 'all' in panel['regions'] or region in panel['regions'] else 'out_of_region')
        species_status = 'context_matches' if panel['species'] == species else 'out_of_species'
        rows.append(dict(panel_id=panel['id'], label=panel['label'], category=panel['category'],
                         region_status=region_status, species_status=species_status,
                         positive_assayed=';'.join(sorted(positive & genes)),
                         positive_missing=';'.join(sorted(positive - genes)),
                         positive_coverage=len(positive & genes) / len(positive) if positive else 'NA',
                         negative_assayed=';'.join(sorted(negative & genes)),
                         negative_missing=';'.join(sorted(negative - genes)),
                         negative_expression_status='unknown_not_tested',
                         annotation_status='not_performed', stage=panel['stage']))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--genes', type=Path, required=True)
    parser.add_argument('--gene-column')
    parser.add_argument('--region', required=True,
                        choices=['unknown', 'midbrain', 'substantia_nigra', 'cortex', 'striatum', 'cerebellum', 'hippocampus', 'hypothalamus', 'hindbrain'])
    parser.add_argument('--species', required=True, choices=['human', 'mouse', 'macaque', 'marmoset'])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Output exists; choose a new path, no overwrite performed')
    with args.genes.open(encoding='utf-8-sig') as stream:
        if args.gene_column:
            reader = csv.DictReader(stream, delimiter='\t')
            if args.gene_column not in (reader.fieldnames or []):
                raise ValueError('Requested gene column is absent')
            genes = {row[args.gene_column].strip() for row in reader if row[args.gene_column].strip()}
        else:
            genes = {line.strip() for line in stream if line.strip() and not line.startswith('#')}
    if not genes:
        raise ValueError('Empty gene list')
    panels = json.loads((ROOT / 'assets/curated_panels.json').read_text(encoding='utf-8'))['panels']
    rows = audit(panels, genes, args.region, args.species)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    print(f'Audited {len(rows)} panels; no expression, identity or negative-expression calls performed')


if __name__ == '__main__':
    main()
