import io
import json
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_coverage import audit
from import_resources import parse_siletti
from validate_package import validate


def archive(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w') as z:
        for path, content in files.items():
            z.writestr('repo/' + path, content)
    return stream.getvalue()


class BehaviorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.panels = json.loads((ROOT / 'assets/curated_panels.json').read_text(encoding='utf-8'))['panels']

    def row(self, identity, genes, region='midbrain', species='human'):
        return next(r for r in audit(self.panels, set(genes), region, species) if r['panel_id'] == identity)

    def test_missing_negative_not_proven_absent(self):
        row = self.row('da-core', ['TH', 'SLC6A3'])
        self.assertIn('DBH', row['negative_missing'])
        self.assertEqual(row['negative_expression_status'], 'unknown_not_tested')

    def test_measured_negative_still_not_expression_call(self):
        row = self.row('da-core', ['TH', 'SLC6A3', 'DBH'])
        self.assertEqual(row['negative_expression_status'], 'unknown_not_tested')
        self.assertEqual(row['annotation_status'], 'not_performed')

    def test_single_marker_cannot_classify(self):
        self.assertEqual(self.row('da-core', ['TH'])['annotation_status'], 'not_performed')

    def test_full_gene_coverage_cannot_classify(self):
        self.assertEqual(self.row('da-core', ['TH', 'DDC', 'SLC6A3', 'SLC18A2'])['positive_coverage'], 1)
        self.assertEqual(self.row('da-core', ['TH', 'DDC', 'SLC6A3', 'SLC18A2'])['annotation_status'], 'not_performed')

    def test_cortical_panel_not_midbrain_type(self):
        self.assertEqual(self.row('cortical-pvalb', ['PVALB'])['region_status'], 'out_of_region')

    def test_cortical_region_permits_review_only(self):
        row = self.row('cortical-pvalb', ['PVALB'], region='cortex')
        self.assertEqual(row['region_status'], 'context_matches')
        self.assertEqual(row['annotation_status'], 'not_performed')

    def test_species_not_silently_transferred(self):
        self.assertEqual(self.row('da-core', ['TH'], species='mouse')['species_status'], 'out_of_species')

    def test_case_not_ortholog_mapping(self):
        self.assertEqual(self.row('da-core', ['Th', 'Slc6a3'])['positive_coverage'], 0)

    def test_unknown_region_remains_unknown(self):
        self.assertEqual(self.row('cortical-pvalb', ['PVALB'], region='unknown')['region_status'], 'review_required_unknown_region')

    def test_peptide_separate_from_identity(self):
        self.assertEqual(self.row('peptide-sst', ['SST'])['category'], 'neuropeptide_program')
        self.assertEqual(self.row('cortical-sst', ['SST'])['category'], 'regional_subtype')

    def test_aggregate_gene_coverage_not_cell_coexpression(self):
        row = self.row('gaba-core', ['GAD1', 'GAD2', 'SLC32A1'])
        self.assertNotIn('coexpression', row)
        self.assertEqual(row['annotation_status'], 'not_performed')

    def test_path_identity_preserves_alternative_rules(self):
        source = archive({
            'Human_adult/Neurotransmission/NT-GABA1.md': 'name: GABAergic\nabbreviation: NT-GABA\ndefinition: +GAD1 +SLC32A1 -SLC6A5\n---\n',
            'Human_adult/Neurotransmission/NT-GABA2.md': 'name: GABAergic\nabbreviation: NT-GABA\ndefinition: +GAD2 +SLC32A1 -SLC6A5\n---\n'})
        panels, markers, licenses = parse_siletti(source)
        self.assertEqual(len(panels), 2)
        self.assertEqual(len({p['panel_id'] for p in panels}), 2)
        self.assertEqual(sum(m['polarity'] == 'source_negative' for m in markers), 2)
        self.assertEqual(licenses, [])

    def test_peptide_source_is_program(self):
        panels, _, _ = parse_siletti(archive({'Neuropeptides/NP-IGF1.md': 'name: IGF1\nabbreviation: IGF1\ndefinition: +IGF1\n---\n'}))
        self.assertEqual(panels[0]['review_category'], 'neuropeptide_program')

    def test_unknown_rule_syntax_rejected(self):
        with self.assertRaises(ValueError):
            parse_siletti(archive({'Human_adult/Class/test.md': 'name: test\ndefinition: +GAD1 OR +GAD2\n'}))

    def test_metadata_inconsistency_is_preserved(self):
        panels, _, _ = parse_siletti(archive({'Human_adult/Subtype/Neuronal/CB-GRAN.md': 'name: granule\ndefinition: +CBLN1\ncategories: Glial\n'}))
        self.assertEqual(panels[0]['source_category_raw'], 'Glial')
        self.assertEqual(panels[0]['review_category'], 'source_regional_subtype')

    def test_dependent_source_family_not_independent(self):
        sources = {s['source_id']: s for s in json.loads((ROOT / 'assets/source_registry.json').read_text(encoding='utf-8'))['sources']}
        self.assertEqual(sources['siletti_rules']['evidence_family'], sources['siletti_atlas']['evidence_family'])

    def test_package_source_trace(self):
        result = validate()
        self.assertEqual(result['status'], 'PASS')
        self.assertFalse(result['biological_classifier_validated'])


if __name__ == '__main__':
    unittest.main()
