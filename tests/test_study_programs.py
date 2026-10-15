"""Boundary checks for the newly sourced neuronal support and programs."""
import json
import unittest
from pathlib import Path
from test_review_rules import MOD, evidence

ROOT = Path(__file__).resolve().parents[1]

class StudyProgramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = {r['id']: r for r in MOD.load_rules(ROOT)}

    def test_nrgn_cannot_replace_neuronal_core(self):
        rule = self.rules['neuronal-background']
        ev = evidence(rule)
        for gene, row in ev['gene_evidence'].items():
            row['state'] = 'supported' if gene == 'NRGN' else 'undetermined'
        result = MOD.review_evidence(rule, ev)
        self.assertNotEqual(result['review_grade'], 'High')

    def test_rit2_program_does_not_require_galntl6_or_da_core(self):
        rule = self.rules['rit2-enriched-program']
        ev = evidence(rule)
        for gene, row in ev['gene_evidence'].items():
            row['state'] = 'supported' if gene == 'RIT2' else 'undetermined'
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result['review_grade'], 'High')
        self.assertEqual(result['claim_kind'], 'program')
        self.assertNotIn('GALNTL6', ev['gene_evidence'])

    def test_galntl6_cannot_be_filled_by_nrgn(self):
        rule = self.rules['galntl6-associated-program']
        ev = evidence(rule)
        for gene, row in ev['gene_evidence'].items():
            row['state'] = 'supported' if gene == 'NRGN' else 'undetermined'
        self.assertNotEqual(MOD.review_evidence(rule, ev)['review_grade'], 'High')

    def test_program_support_does_not_fill_da_identity(self):
        rule = self.rules['da-core']
        ev = evidence(rule)
        for row in ev['gene_evidence'].values():
            row['state'] = 'undetermined'
        result = MOD.review_evidence(rule, ev)
        self.assertNotEqual(result['review_grade'], 'High')

    def test_source_scope_not_silently_transferred_to_cortex(self):
        rule = self.rules['rit2-enriched-program']
        ev = evidence(rule);ev['region'] = 'cortex'
        self.assertEqual(MOD.review_evidence(rule, ev)['review_grade'], 'NotApplicable')

if __name__ == '__main__':
    unittest.main()
