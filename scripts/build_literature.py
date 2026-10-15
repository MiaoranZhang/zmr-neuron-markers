"""Regenerate literature provenance from the adopted marker assertions and citations."""
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def build(root=ROOT):
    bib={x['source_id']:x for x in json.loads((root/'assets/literature_registry.json').read_text(encoding='utf-8'))['citations']}
    sources={x['source_id']:x for x in json.loads((root/'assets/source_registry.json').read_text(encoding='utf-8'))['sources']}
    rules=sum([json.loads(p.read_text(encoding='utf-8')) for p in sorted((root/'assets/rules').glob('*.json'))],[])
    with (root/'assets/curated_marker_assertions.tsv').open(encoding='utf-8',newline='') as stream:
        assertions=list(csv.DictReader(stream,delimiter='\t'))
    rows=[]
    for x in assertions:
        g=x['gene_symbol_raw'];citation=bib[x['source_id']]
        rows.append(dict(gene_symbol=g,panel_id=x['panel_id'],curated_role=x['curated_role'],source_id=x['source_id'],
            **{k:citation[k] for k in ['authors','title','journal','year','doi']},paper_url='https://doi.org/'+citation['doi'],source_locator=x['source_locator'],source_url=x['source_url'],source_version=x['source_version'],evidence_family=x['evidence_family'],evidence_kind=citation['evidence_kind'],source_species_context=x['source_species_context'],
            core_rule_ids=';'.join(r['id'] for r in rules if any(g in group for route in r['core_routes'] for group in route['all_of'])),
            supporting_rule_ids=';'.join(r['id'] for r in rules if g in r['supporting']['genes']),
            conflict_rule_ids=';'.join(r['id'] for r in rules if any(g in z['genes'] for z in r['conflicts'])),
            original_marker_discovery_paper='NA_not_claimed_unless_source_locator_establishes_it'))
    with (root/'assets/marker_literature.tsv').open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
    return {'n_literature_rows':len(rows),'n_genes':len({r['gene_symbol'] for r in rows})}

if __name__=='__main__':
    print(json.dumps(build(),ensure_ascii=False))
