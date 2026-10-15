"""Synthetic boundary checks; none measure annotation accuracy in real cells."""
import copy
import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts/review_rules.py"
SPEC = importlib.util.spec_from_file_location("review_rules", PATH)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def fixture():
    return {
        "id": "gaba-core", "target_label": "GABAergic", "level": "transmitter",
        "claim_kind": "identity", "scope": {"species": "human", "stage": "adult", "regions": ["all"]},
        "parent": None,
        "core_routes": [
            {"id": "gad1", "all_of": [["GAD1"], ["SLC32A1"]], "basis": "curated", "note": "synthetic"},
            {"id": "gad2", "all_of": [["GAD2"], ["SLC32A1"]], "basis": "curated", "note": "synthetic"}],
        "supporting": {"genes": ["SLC6A1"], "panel_ids": [], "use": "support only"},
        "conflicts": [{"program": "alternative", "genes": ["SLC6A5"],
                       "interpretation": "contextual", "action": "review_not_single_gene_veto"}],
        "high_requires": ["Same-unit coordinated program", "Competing programs reviewed"],
        "confidence_cap": "High", "fallback": {"missing_core": "retain parent",
            "strong_conflict": "uncertain", "fallback_label": "Uncertain"},
        "rescue_routes": [], "validation_status": "curated_unbenchmarked",
        "source_panel_ids": ["gaba-core"], "notes": "Synthetic test only",
    }


def evidence(rule=None):
    rule = rule or fixture()
    result = MOD.evidence_template(rule)
    result.update(unit_type="cluster", unit_id="synthetic-1", species="human", stage="adult", region="midbrain",
                  reviewer="synthetic-reviewer", review_date="2026-10-15")
    for gene, row in result["gene_evidence"].items():
        row.update(unit_type="cluster", unit_id="synthetic-1", evidence_ref="synthetic/manual-review",
                   state="supported" if gene in {"GAD1", "SLC32A1"} else "undetermined")
    for row in list(result["gates"].values()) + result["rule_checks"]:
        row.update(status="pass", evidence_refs=["synthetic/review"])
    if result["parent_evidence"]:
        result["parent_evidence"].update(confidence="High", reviewed_record_id="parent-record",
            unit_type="cluster", unit_id="synthetic-1", evidence_refs=["synthetic/parent"])
    return result


class ReviewBehavior(unittest.TestCase):
    def test_complete_review_is_not_probability(self):
        result = MOD.review_evidence(fixture(), evidence())
        self.assertEqual(result["review_grade"], "High")
        self.assertFalse(result["biological_classifier_validated"])
        self.assertFalse(result["writes_cell_labels"])
        self.assertEqual(result["rulebook_version"], "1.2.0")
        self.assertIsNone(result["fallback_guidance"])

    def test_high_requires_reviewer_and_valid_calendar_date(self):
        for field, value in (("reviewer", ""), ("reviewer", "  "), ("reviewer", None),
                             ("review_date", ""), ("review_date", "yesterday"),
                             ("review_date", "2026-02-30"), ("review_date", "20261015")):
            ev = evidence()
            ev[field] = value
            with self.subTest(field=field, value=value):
                result = MOD.review_evidence(fixture(), ev)
                self.assertEqual(result["review_grade"], "Moderate")
                self.assertTrue(result["candidate_only"])

    def test_all_unknown_template_never_assigns_catalog_fallback(self):
        rule = fixture()
        rule["fallback"]["fallback_label"] = "Neuron"
        ev = MOD.evidence_template(rule)
        ev["unit_id"] = "synthetic-unknown"
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result["review_grade"], "Low")
        self.assertEqual(result["suggested_review_label"], "Unknown/Uncertain")
        self.assertIsNone(result["candidate_only"])

    def test_missing_parent_and_core_cannot_suggest_parent_label(self):
        rule = fixture()
        rule["parent"] = {"panel_id": "neuronal-background", "minimum_confidence": "High"}
        rule["fallback"]["fallback_label"] = "Neuron"
        ev = evidence(rule)
        ev["parent_evidence"] = None
        for row in ev["gene_evidence"].values():
            row["state"] = "not_assayed"
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result["suggested_review_label"], "Unknown/Uncertain")
        self.assertFalse(result["parent_review"]["same_unit_high_record_documented"])

    def test_missing_parent_keeps_complete_core_explicitly_candidate(self):
        rule = fixture()
        rule["parent"] = {"panel_id": "neuronal-background", "minimum_confidence": "High"}
        ev = evidence(rule)
        ev["parent_evidence"] = None
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertIn("[parent not established]", result["suggested_review_label"])
        self.assertTrue(result["suggested_review_label"].endswith("[candidate]"))

    def test_low_records_documented_parent_without_inheriting_its_label(self):
        rule = fixture()
        rule["parent"] = {"panel_id": "neuronal-background", "minimum_confidence": "High"}
        rule["fallback"]["fallback_label"] = "Neuron"
        ev = evidence(rule)
        for row in ev["gene_evidence"].values():
            row["state"] = "undetermined"
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result["suggested_review_label"], "Unknown/Uncertain")
        self.assertTrue(result["parent_review"]["same_unit_high_record_documented"])
        self.assertFalse(result["parent_review"]["retained_as_suggested_label"])

    def test_failed_quality_or_strong_conflict_does_not_retain_parent_label(self):
        rule = fixture()
        rule["parent"] = {"panel_id": "neuronal-background", "minimum_confidence": "High"}
        rule["fallback"]["fallback_label"] = "Neuron"
        for failure in ("quality", "conflict"):
            ev = evidence(rule)
            if failure == "quality":
                ev["gates"]["data_quality"]["status"] = "fail"
            else:
                ev["unresolved_strong_conflict"] = True
            with self.subTest(failure=failure):
                result = MOD.review_evidence(rule, ev)
                self.assertEqual(result["suggested_review_label"], "Unknown/Uncertain")
                self.assertIsNone(result["candidate_only"])
                self.assertTrue(result["parent_review"]["requires_reassessment_before_reuse"])

    def test_missing_or_old_rulebook_version_rejected(self):
        for version in (None, "1.0.0", "1.1.0"):
            ev = evidence()
            ev["rulebook_version"] = version
            with self.subTest(version=version), self.assertRaisesRegex(ValueError, "version"):
                MOD.review_evidence(fixture(), ev)

    def test_gaba_routes_are_alternatives(self):
        ev = evidence()
        ev["gene_evidence"]["GAD1"]["state"] = "not_assayed"
        ev["gene_evidence"]["GAD2"]["state"] = "supported"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "High")

    def test_any_inside_all_groups(self):
        rule = fixture()
        rule["core_routes"] = [{"id": "either-gad", "all_of": [["GAD1", "GAD2"], ["SLC32A1"]],
                                "basis": "curated", "note": "synthetic"}]
        self.assertEqual(MOD.review_evidence(rule, evidence(rule))["review_grade"], "High")

    def test_auxiliary_cannot_replace_missing_core(self):
        ev = evidence()
        ev["gene_evidence"]["SLC32A1"]["state"] = "not_assayed"
        ev["gene_evidence"]["SLC6A1"]["state"] = "supported"
        result = MOD.review_evidence(fixture(), ev)
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertFalse(result["supporting_genes_replace_core"])
        self.assertEqual(result["suggested_review_label"],
                         "Unknown/Uncertain at assessed level (partial core evidence)")
        self.assertEqual(result["decision_status"], "partial_core_review_required")
        self.assertFalse(result["type_specific_candidate"])
        self.assertTrue(result["partial_core_not_type_specific"])
        self.assertTrue(result["candidate_only"])

    def test_any_incomplete_core_cannot_suggest_assessed_type(self):
        rule = fixture()
        for retained in ("GAD1", "GAD2", "SLC32A1"):
            ev = evidence(rule)
            for gene, row in ev["gene_evidence"].items():
                row["state"] = "supported" if gene == retained else "undetermined"
            with self.subTest(retained=retained):
                result = MOD.review_evidence(rule, ev)
                self.assertNotIn(rule["target_label"], result["suggested_review_label"])
                self.assertFalse(result["type_specific_candidate"])
                self.assertEqual(result["rule_specific_fallback_guidance"]["text"],
                                 rule["fallback"]["missing_core"])

    def test_complete_core_with_incomplete_review_remains_specific_candidate(self):
        ev = evidence()
        ev["gates"]["discrimination"]["status"] = "unknown"
        result = MOD.review_evidence(fixture(), ev)
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertTrue(result["suggested_review_label"].endswith(" [candidate]"))
        self.assertTrue(result["type_specific_candidate"])
        self.assertFalse(result["partial_core_not_type_specific"])

    def test_only_auxiliary_is_low(self):
        ev = evidence()
        for entry in ev["gene_evidence"].values():
            entry["state"] = "undetermined"
        ev["gene_evidence"]["SLC6A1"]["state"] = "supported"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Low")

    def test_missing_gene_not_negative(self):
        ev = evidence()
        del ev["gene_evidence"]["SLC32A1"]
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Moderate")

    def test_scope_mismatch(self):
        ev = evidence()
        ev["species"] = "mouse"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "NotApplicable")

    def test_region_not_generalized(self):
        rule = fixture()
        rule["scope"]["regions"] = ["cortex"]
        rule["fallback"]["fallback_label"] = "Cortical GABAergic"
        result = MOD.review_evidence(rule, evidence(rule))
        self.assertEqual(result["review_grade"], "NotApplicable")
        self.assertIsNone(result["suggested_review_label"])
        self.assertIsNone(result["candidate_only"])
        self.assertEqual(result["decision_status"], "rule_not_applicable")

    def test_unknown_scope_blocks_high(self):
        ev = evidence()
        ev["region"] = "unknown"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Moderate")

    def test_parent_must_be_high_same_unit_and_correct_id(self):
        rule = fixture()
        rule["parent"] = {"panel_id": "neuronal-background", "minimum_confidence": "High"}
        for field, value in [("confidence", "Moderate"), ("panel_id", "da-core"),
                             ("unit_type", "cell"), ("unit_id", "other"),
                             ("evidence_refs", []), ("reviewed_record_id", "")]:
            ev = evidence(rule)
            ev["parent_evidence"][field] = value
            with self.subTest(field=field):
                self.assertEqual(MOD.review_evidence(rule, ev)["review_grade"], "Moderate")

    def test_single_cell_evidence_cannot_stand_in_for_whole_cluster(self):
        ev = evidence()
        ev["gene_evidence"]["SLC32A1"]["unit_type"] = "cell"
        result = MOD.review_evidence(fixture(), ev)
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertEqual(result["ignored_supported_gene_evidence"]["SLC32A1"], "different_review_unit")

    def test_per_cell_identity_rejected_even_with_complete_review(self):
        ev = evidence()
        ev['unit_type'] = 'cell'
        for row in ev['gene_evidence'].values():
            row['unit_type'] = 'cell'
        with self.assertRaisesRegex(ValueError, 'formal cluster'):
            MOD.review_evidence(fixture(), ev)

    def test_cell_program_diagnostic_does_not_become_identity(self):
        rule = fixture()
        rule.update(claim_kind='program', level='program')
        ev = evidence(rule)
        ev['unit_type'] = 'cell'
        for row in ev['gene_evidence'].values():
            row['unit_type'] = 'cell'
        result = MOD.review_evidence(rule, ev)
        self.assertEqual(result['claim_kind'], 'program')
        self.assertFalse(result['writes_cell_labels'])

    def test_cluster_review_can_be_high_for_cluster(self):
        ev = evidence()
        ev["unit_type"] = "cluster"
        for row in ev["gene_evidence"].values():
            row["unit_type"] = "cluster"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "High")

    def test_unreferenced_supported_gene_is_not_evidence(self):
        ev = evidence()
        ev["gene_evidence"]["GAD1"]["evidence_ref"] = ""
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Moderate")

    def test_gates_need_evidence_and_pass(self):
        for gate in MOD.GATES:
            ev = evidence()
            ev["gates"][gate]["evidence_refs"] = []
            with self.subTest(gate=gate):
                self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Moderate")

    def test_failed_quality_or_conflict_is_low(self):
        for gate in ("data_quality", "conflict_review", "discrimination"):
            ev = evidence()
            ev["gates"][gate]["status"] = "fail"
            with self.subTest(gate=gate):
                self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Low")

    def test_strong_conflict_overrides_passed_gates(self):
        ev = evidence()
        ev["unresolved_strong_conflict"] = True
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Low")

    def test_single_context_conflict_gene_not_automatic_veto(self):
        ev = evidence()
        ev["gene_evidence"]["SLC6A5"]["state"] = "supported"
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "High")

    def test_omitted_rule_requirement_blocks_high(self):
        ev = evidence()
        ev["rule_checks"].pop()
        self.assertEqual(MOD.review_evidence(fixture(), ev)["review_grade"], "Moderate")

    def test_unknown_requirement_rejected(self):
        ev = evidence()
        ev["rule_checks"][0]["requirement"] = "Invented replacement"
        with self.assertRaises(ValueError):
            MOD.review_evidence(fixture(), ev)

    def test_confidence_cap(self):
        rule = fixture()
        rule["confidence_cap"] = "Moderate"
        self.assertEqual(MOD.review_evidence(rule, evidence(rule))["review_grade"], "Moderate")

    def test_program_high_remains_program(self):
        rule = fixture()
        rule["claim_kind"] = "program"
        rule["level"] = "program"
        result = MOD.review_evidence(rule, evidence(rule))
        self.assertEqual(result["review_grade"], "High")
        self.assertEqual(result["claim_kind"], "program")

    def test_replication_and_validation_never_raise_grade(self):
        ev = evidence()
        ev["gene_evidence"]["SLC32A1"]["state"] = "not_assayed"
        ev["donor_replication"] = {"status": "replicated", "evidence_refs": ["donors"]}
        ev["independent_validation"] = {"status": "validated", "evidence_refs": ["same-used-marker"]}
        result = MOD.review_evidence(fixture(), ev)
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertIn("independence_not_documented",
                      result["separate_evidence_ledgers"]["independent_validation"]["warnings"])

    def test_no_input_mutation(self):
        rule, ev = fixture(), evidence()
        before = copy.deepcopy((rule, ev))
        MOD.review_evidence(rule, ev)
        self.assertEqual((rule, ev), before)


class StructuralBehavior(unittest.TestCase):
    def validate(self, rules):
        panels = [{"id": r["id"]} for r in rules]
        genes = {"GAD1", "GAD2", "SLC32A1", "SLC6A1", "SLC6A5"}
        rows = [{"panel_id": p["id"], "gene_symbol_raw": gene, "curated_role": "positive",
                 "source_locator": "synthetic", "source_url": "https://example.org/synthetic"}
                for p in panels for gene in genes]
        return MOD.validate_rules(rules=rules, panels=panels, assertion_rows=rows)

    def test_valid_structure(self):
        self.assertEqual(self.validate([fixture()])["status"], "PASS")

    def test_invalid_level_or_kind_pair_rejected(self):
        for level, kind in (("unsupported", "identity"), ("program", "identity"),
                            ("major", "program")):
            rule = fixture()
            rule.update(level=level, claim_kind=kind)
            with self.subTest(level=level, kind=kind), self.assertRaises(ValueError):
                self.validate([rule])

    def test_single_gene_conflict_veto_prohibited(self):
        rule = fixture()
        rule["conflicts"][0]["action"] = "single_gene_veto"
        with self.assertRaisesRegex(ValueError, "conflict"):
            self.validate([rule])

    def test_untraced_gene_rejected(self):
        rule = fixture()
        rule["core_routes"][0]["all_of"].append(["UNTRACED"])
        with self.assertRaisesRegex(ValueError, "provenance"):
            self.validate([rule])

    def test_rescue_is_not_silently_accepted(self):
        rule = fixture()
        rule["rescue_routes"] = [{"id": "invented"}]
        with self.assertRaisesRegex(ValueError, "rescue"):
            self.validate([rule])

    def test_parent_cycles_rejected(self):
        first, second = fixture(), fixture()
        second["id"] = "parent"
        second["source_panel_ids"] = ["parent"]
        first["parent"] = {"panel_id": "parent", "minimum_confidence": "High"}
        second["parent"] = {"panel_id": "gaba-core", "minimum_confidence": "High"}
        with self.assertRaisesRegex(ValueError, "cycle"):
            self.validate([first, second])

    def test_duplicate_rule_rejected(self):
        with self.assertRaises(ValueError):
            self.validate([fixture(), fixture()])


class ProductionPartialCoreBehavior(unittest.TestCase):
    """Actual shipped rules, synthetic reviewed inputs; no biological validation."""

    @classmethod
    def setUpClass(cls):
        cls.rules = {r["id"]: r for r in MOD.load_rules()}

    def reviewed_genes(self, rule_id, supported_genes):
        rule = self.rules[rule_id]
        ev = evidence(rule)
        for gene, row in ev["gene_evidence"].items():
            row["state"] = "supported" if gene in supported_genes else "undetermined"
        return MOD.review_evidence(rule, ev)

    def assert_partial_unresolved(self, rule_id, result):
        self.assertEqual(result["review_grade"], "Moderate")
        self.assertEqual(result["decision_status"], "partial_core_review_required")
        self.assertTrue(result["partial_core_not_type_specific"])
        self.assertFalse(result["type_specific_candidate"])
        self.assertTrue(result["candidate_only"])
        self.assertEqual(result["suggested_review_label"],
                         "Unknown/Uncertain at assessed level (partial core evidence)")
        self.assertNotIn(self.rules[rule_id]["target_label"], result["suggested_review_label"])
        self.assertTrue(any(r["unsatisfied_groups"] for r in result["core_routes"]))

    def test_ddc_alone_cannot_generate_four_monoamine_candidates(self):
        for rule_id in ("da-core", "noradrenergic", "adrenergic", "serotonergic"):
            with self.subTest(rule_id=rule_id):
                self.assert_partial_unresolved(rule_id, self.reviewed_genes(rule_id, {"DDC"}))

    def test_shared_slc32a1_cannot_generate_glycinergic_candidate(self):
        self.assert_partial_unresolved("glycinergic", self.reviewed_genes("glycinergic", {"SLC32A1"}))

    def test_ne_core_without_pnmt_cannot_generate_adrenergic_candidate(self):
        genes = {"TH", "DDC", "DBH"}
        result = self.reviewed_genes("adrenergic", genes)
        self.assert_partial_unresolved("adrenergic", result)
        self.assertIn(["PNMT"], result["core_routes"][0]["unsatisfied_groups"])
        ne_result = self.reviewed_genes("noradrenergic", genes)
        self.assertFalse(ne_result["partial_core_not_type_specific"])
        self.assertTrue(any(route["satisfied"] for route in ne_result["core_routes"]))


if __name__ == "__main__":
    unittest.main()
