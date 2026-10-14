"""Check human-reviewed marker evidence; never read expression or assign cell labels.

The rule combinations are curated, unbenchmarked review criteria. A High result
means that the supplied review record passes these criteria, not that biology or
the truth of a supplied evidence reference has been independently verified.
"""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULEBOOK_VERSION = "1.1.0"
STATUSES = {"pass", "fail", "unknown"}
GENE_STATES = {"supported", "not_supported", "not_assayed", "undetermined"}
GATES = ("applicability", "data_quality", "discrimination", "conflict_review")
UNKNOWN = {"", "unknown", "unspecified", "not_available", None}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _strings(value, allow_empty=False):
    return (isinstance(value, list) and (bool(value) or allow_empty)
            and all(_text(x) for x in value) and len(value) == len(set(value)))


def _refs(value):
    return _strings(value)


def _check_rulebook_version(value):
    _require(value == RULEBOOK_VERSION,
             "Rulebook version missing or incompatible; re-review using version " + RULEBOOK_VERSION)


def load_rules(root=ROOT):
    """Load all JSON rule arrays in assets/rules, preserving their order."""
    root = Path(root)
    paths = sorted((root / "assets/rules").glob("*.json"))
    _require(bool(paths), "No rule arrays found in assets/rules")
    rules = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        _require(isinstance(data, list), f"Rule file must be an array: {path.name}")
        rules.extend(data)
    return rules


def validate_rules(root=ROOT, rules=None, panels=None, assertion_rows=None):
    """Validate structure and catalog provenance, not biological performance.

    Optional panels/assertion_rows support isolated synthetic behavioral tests.
    Production invocation checks the frozen 37-panel, 74-gene starter catalog.
    """
    root = Path(root)
    if rules is None:
        rules = load_rules(root)
    production_catalog = panels is None
    if production_catalog:
        manifest = json.loads((root / "assets/rulebook_manifest.json").read_text(encoding="utf-8-sig"))
        _check_rulebook_version(manifest.get("rulebook_version"))
    if panels is None:
        panels = json.loads((root / "assets/curated_panels.json").read_text(
            encoding="utf-8-sig"))["panels"]
    if assertion_rows is None:
        with (root / "assets/curated_marker_assertions.tsv").open(
                encoding="utf-8-sig", newline="") as stream:
            assertion_rows = list(csv.DictReader(stream, delimiter="\t"))
    panel_ids = {p["id"] for p in panels}
    _require(len(panel_ids) == len(panels), "Duplicate catalog panel IDs")
    traced = {p: set() for p in panel_ids}
    positive_traced = {p: set() for p in panel_ids}
    for row in assertion_rows:
        _require(row.get("panel_id") in traced, "Unknown panel in source assertions")
        _require(_text(row.get("source_locator")) and
                 _text(row.get("source_url")), "Missing source assertion locator")
        traced[row["panel_id"]].add(row["gene_symbol_raw"])
        if row.get("curated_role") == "positive":
            positive_traced[row["panel_id"]].add(row["gene_symbol_raw"])
    catalog_genes = set().union(*traced.values())
    if production_catalog:
        _require(len(panel_ids) == 37 and len(catalog_genes) == 74,
                 "Expected the version 1.1 frozen 37-panel, 74-gene catalog")
    _require(isinstance(rules, list) and bool(rules), "Rules must be a nonempty array")
    _require(all(isinstance(r, dict) for r in rules), "Each rule must be an object")
    ids = [r.get("id") for r in rules]
    _require(all(_text(x) for x in ids) and len(ids) == len(set(ids)),
             "Missing or duplicate rule IDs")
    _require(set(ids) == panel_ids, "Every catalog panel must have exactly one rule")
    by_id = {r["id"]: r for r in rules}
    for rule in rules:
        rid = rule["id"]
        required = {"id", "target_label", "level", "claim_kind", "scope", "parent",
                    "core_routes", "supporting", "conflicts", "high_requires",
                    "confidence_cap", "fallback", "rescue_routes", "validation_status",
                    "source_panel_ids", "notes"}
        _require(required <= set(rule), f"{rid}: missing required rule fields")
        _require(_text(rule["target_label"]) and _text(rule["level"]),
                 f"{rid}: missing target or level")
        _require(rule["claim_kind"] in {"identity", "program"}, f"{rid}: invalid claim kind")
        _require(rule["level"] in {"major", "transmitter", "subtype", "program"},
                 f"{rid}: invalid annotation level")
        _require((rule["claim_kind"] == "program") == (rule["level"] == "program"),
                 f"{rid}: claim kind and annotation level are inconsistent")
        scope = rule["scope"]
        _require(isinstance(scope, dict) and set(scope) == {"species", "stage", "regions"},
                 f"{rid}: invalid scope fields")
        for key in ("species", "stage"):
            _require(_text(scope[key]) or _strings(scope[key]), f"{rid}: invalid {key}")
        _require(_strings(scope["regions"]), f"{rid}: missing regions")
        _require(_strings(rule["source_panel_ids"]) and
                 set(rule["source_panel_ids"]) <= panel_ids and
                 rid in rule["source_panel_ids"], f"{rid}: invalid source panel IDs")
        allowed = set().union(*(traced[p] for p in rule["source_panel_ids"]))
        positive = set().union(*(positive_traced[p] for p in rule["source_panel_ids"]))
        parent = rule["parent"]
        if parent is not None:
            _require(isinstance(parent, dict) and parent.get("panel_id") in by_id and
                     parent["panel_id"] != rid and parent.get("minimum_confidence") == "High",
                     f"{rid}: invalid parent")
        routes = rule["core_routes"]
        _require(isinstance(routes, list) and bool(routes), f"{rid}: empty core routes")
        route_ids = []
        used = set()
        for route in routes:
            _require(isinstance(route, dict) and _text(route.get("id")) and
                     _text(route.get("basis")) and _text(route.get("note")),
                     f"{rid}: invalid core route")
            route_ids.append(route["id"])
            groups = route.get("all_of")
            _require(isinstance(groups, list) and bool(groups) and
                     all(_strings(g) for g in groups), f"{rid}: invalid all_of groups")
            genes = {g for group in groups for g in group}
            _require(genes <= positive, f"{rid}: core genes lack positive source-panel provenance")
            used.update(genes)
        _require(len(route_ids) == len(set(route_ids)), f"{rid}: duplicate core route IDs")
        support = rule["supporting"]
        _require(isinstance(support, dict) and _strings(support.get("genes"), True) and
                 _strings(support.get("panel_ids"), True) and _text(support.get("use")),
                 f"{rid}: invalid supporting evidence")
        _require(set(support["panel_ids"]) <= panel_ids, f"{rid}: unknown supporting panel")
        used.update(support["genes"])
        _require(isinstance(rule["conflicts"], list), f"{rid}: invalid conflicts")
        for conflict in rule["conflicts"]:
            _require(isinstance(conflict, dict) and _text(conflict.get("program")) and
                     _strings(conflict.get("genes"), True) and
                     _text(conflict.get("interpretation")) and
                     conflict.get("action") == "review_not_single_gene_veto",
                     f"{rid}: invalid conflict record")
            used.update(conflict["genes"])
        _require(used <= catalog_genes and used <= allowed,
                 f"{rid}: rule genes not covered by source_panel_ids")
        _require(_strings(rule["high_requires"]), f"{rid}: missing High review requirements")
        _require(rule["confidence_cap"] in {"High", "Moderate"}, f"{rid}: invalid confidence cap")
        fallback = rule["fallback"]
        _require(isinstance(fallback, dict) and all(_text(fallback.get(k)) for k in
                 ("missing_core", "strong_conflict", "fallback_label")), f"{rid}: invalid fallback")
        _require(rule["rescue_routes"] == [], f"{rid}: unvalidated rescue routes are prohibited in v1.1")
        _require(rule["validation_status"] == "curated_unbenchmarked",
                 f"{rid}: unsupported biological validation claim")
        _require(_text(rule["notes"]) or _strings(rule["notes"]), f"{rid}: empty notes")
    for rid in by_id:
        visited = set()
        current = rid
        while current is not None:
            _require(current not in visited, f"Parent cycle containing {rid}")
            visited.add(current)
            parent = by_id[current]["parent"]
            current = parent["panel_id"] if parent else None
    return {"status": "PASS", "n_rules": len(rules), "n_catalog_genes": len(catalog_genes),
            "rulebook_version": RULEBOOK_VERSION,
            "biological_classifier_validated": False,
            "note": "Structure and source coverage only; curated combinations remain unbenchmarked."}


def evidence_template(rule):
    """Return a deliberately incomplete template requiring manual review."""
    genes = {g for route in rule["core_routes"] for group in route["all_of"] for g in group}
    genes.update(rule["supporting"]["genes"])
    genes.update(g for c in rule["conflicts"] for g in c["genes"])
    parent = rule["parent"]
    return {
        "rulebook_version": RULEBOOK_VERSION,
        "rule_id": rule["id"], "unit_type": "cluster", "unit_id": "",
        "species": "unknown", "stage": "unknown", "region": "unknown",
        "parent_evidence": ({"panel_id": parent["panel_id"], "confidence": "Unknown",
                             "reviewed_record_id": "", "unit_type": "cluster", "unit_id": "",
                             "evidence_refs": []} if parent else None),
        "gene_evidence": {g: {"state": "undetermined", "unit_type": "cluster", "unit_id": "",
                              "evidence_ref": ""} for g in sorted(genes)},
        "gates": {key: {"status": "unknown", "evidence_refs": []} for key in GATES},
        "rule_checks": [{"requirement": x, "status": "unknown", "evidence_refs": []}
                        for x in rule["high_requires"]],
        "unresolved_strong_conflict": False,
        "donor_replication": {"status": "unknown", "evidence_refs": []},
        "independent_validation": {"status": "unknown", "evidence_refs": [],
                                   "held_out_from_annotation": None, "evidence_family": ""},
        "reviewer": "", "review_date": "", "notes": "",
    }


def _scope_status(rule, evidence):
    unknown = []
    mismatch = []
    for key, scopekey in (("species", "species"), ("stage", "stage"), ("region", "regions")):
        value = evidence.get(key)
        permitted = rule["scope"][scopekey]
        permitted = [permitted] if isinstance(permitted, str) else permitted
        if value in UNKNOWN:
            unknown.append(key)
        elif value not in permitted and not (set(permitted) & {"all", "any", "unspecified"}):
            mismatch.append(key)
    return mismatch, unknown


def _review_check(record):
    return (isinstance(record, dict) and record.get("status") == "pass"
            and _refs(record.get("evidence_refs")))


def _review_date(value):
    """Require an explicit calendar date without interpreting locale formats."""
    if not _text(value):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def review_evidence(rule, evidence):
    """Grade the completeness of a human review. Do not infer expression states."""
    _require(isinstance(evidence, dict), "Evidence must be an object")
    _check_rulebook_version(evidence.get("rulebook_version"))
    _require(evidence.get("rule_id") == rule["id"], "Evidence rule ID mismatch")
    _require(evidence.get("unit_type") in {"cell", "cluster"}, "unit_type must be cell or cluster")
    _require(_text(evidence.get("unit_id")), "A nonempty unit_id is required")
    for key in ("species", "stage", "region"):
        _require(isinstance(evidence.get(key), str), f"{key} must be a string")
    unit_type, unit_id = evidence["unit_type"], evidence["unit_id"]
    genes = evidence.get("gene_evidence", {})
    _require(isinstance(genes, dict), "gene_evidence must be an object")
    for gene, entry in genes.items():
        _require(_text(gene) and isinstance(entry, dict) and entry.get("state") in GENE_STATES,
                 f"Invalid gene evidence: {gene}")
        _require(entry.get("unit_type") in {"cell", "cluster"}, f"Invalid gene unit type: {gene}")
    gates = evidence.get("gates", {})
    _require(isinstance(gates, dict), "gates must be an object")
    for key, entry in gates.items():
        _require(key in GATES and isinstance(entry, dict) and entry.get("status") in STATUSES,
                 f"Invalid gate: {key}")
    checks = evidence.get("rule_checks", [])
    _require(isinstance(checks, list), "rule_checks must be an array")
    _require(all(isinstance(c, dict) and _text(c.get("requirement")) and
                 c.get("status") in STATUSES for c in checks), "Invalid rule check")
    requirements = [c["requirement"] for c in checks]
    _require(len(requirements) == len(set(requirements)), "Duplicate rule check requirements")
    _require(set(requirements) <= set(rule["high_requires"]), "Unknown rule check requirement")
    _require(isinstance(evidence.get("unresolved_strong_conflict", False), bool),
             "unresolved_strong_conflict must be boolean")

    reasons = []
    reviewer_ok = _text(evidence.get("reviewer"))
    review_date_ok = _review_date(evidence.get("review_date"))
    if not reviewer_ok:
        reasons.append("reviewer_not_recorded")
    if not review_date_ok:
        reasons.append("review_date_missing_or_invalid_YYYY-MM-DD")
    mismatch, unknown_scope = _scope_status(rule, evidence)
    if mismatch:
        reasons.append("scope_mismatch:" + ",".join(mismatch))
    if unknown_scope:
        reasons.append("scope_unknown:" + ",".join(unknown_scope))
    usable_genes = set()
    ignored_genes = {}
    for gene, entry in genes.items():
        if entry["state"] != "supported":
            continue
        if entry.get("unit_type") != unit_type or entry.get("unit_id") != unit_id:
            ignored_genes[gene] = "different_review_unit"
        elif not _text(entry.get("evidence_ref")):
            ignored_genes[gene] = "missing_evidence_reference"
        else:
            usable_genes.add(gene)
    routes = []
    for route in rule["core_routes"]:
        group_support = [sorted(set(group) & usable_genes) for group in route["all_of"]]
        routes.append({"route_id": route["id"], "satisfied": all(bool(s) for s in group_support),
                       "supported_genes_by_group": group_support,
                       "unsatisfied_groups": [group for group, support in zip(
                           route["all_of"], group_support) if not support]})
    complete_core = any(r["satisfied"] for r in routes)
    some_core = any(s for r in routes for s in r["supported_genes_by_group"])
    if not complete_core:
        reasons.append("core_incomplete" if some_core else "no_supported_core")
    parent_ok = True
    if rule["parent"] is not None:
        parent = evidence.get("parent_evidence")
        parent_ok = (isinstance(parent, dict) and
                     parent.get("panel_id") == rule["parent"]["panel_id"] and
                     parent.get("confidence") == "High" and
                     parent.get("unit_type") == unit_type and parent.get("unit_id") == unit_id and
                     _text(parent.get("reviewed_record_id")) and _refs(parent.get("evidence_refs")))
        if not parent_ok:
            reasons.append("parent_high_not_documented_for_same_unit")
    gates_ok = all(_review_check(gates.get(key)) for key in GATES)
    for key in GATES:
        if not _review_check(gates.get(key)):
            reasons.append("gate_not_passed_with_evidence:" + key)
    check_map = {c["requirement"]: c for c in checks}
    checks_ok = all(_review_check(check_map.get(x)) for x in rule["high_requires"])
    if not checks_ok:
        reasons.append("rule_requirements_not_all_passed_with_evidence")
    failed_gate = any(c.get("status") == "fail" for c in gates.values())
    failed_check = any(c.get("status") == "fail" for c in checks)
    strong_conflict = evidence.get("unresolved_strong_conflict", False)
    if strong_conflict:
        reasons.append("unresolved_strong_conflict")
    if failed_gate or failed_check:
        reasons.append("explicit_review_failure")
    high_ready = (reviewer_ok and review_date_ok and not mismatch and not unknown_scope and complete_core and parent_ok and
                  gates_ok and checks_ok and not strong_conflict)
    if mismatch:
        grade = "NotApplicable"
    elif failed_gate or failed_check or strong_conflict or not some_core:
        grade = "Low"
    elif high_ready and rule["confidence_cap"] == "High":
        grade = "High"
    else:
        grade = "Moderate"
    if high_ready and rule["confidence_cap"] != "High":
        reasons.append("rule_confidence_cap:" + rule["confidence_cap"])

    # Fallback labels are narrative guidance for a human, not evidence that a
    # parent identity was established. Never turn them into an automatic label.
    if grade == "High":
        suggested_label = rule["target_label"]
        decision_status = "review_complete_for_assessed_level"
        guidance = ("The supplied review meets this rule at the assessed level. "
                    "This is not independent verification of the evidence or biological identity.")
    elif grade == "Moderate" and not complete_core:
        suggested_label = "Unknown/Uncertain at assessed level (partial core evidence)"
        decision_status = "partial_core_review_required"
        guidance = ("Only partial core evidence is documented. Moderate describes review completeness "
                    "and does not support a type-specific candidate at this level. Inspect missing "
                    "core groups and the human-only rule guidance; no parent label is inherited.")
    elif grade == "Moderate":
        parent_note = " [parent not established]" if rule["parent"] and not parent_ok else ""
        suggested_label = rule["target_label"] + parent_note + " [candidate]"
        decision_status = "candidate_requires_review"
        guidance = ("Candidate only: resolve the listed reasons before accepting this assessed level. "
                    "No parent identity is inferred from this candidate result.")
    elif grade == "Low":
        suggested_label = "Unknown/Uncertain"
        decision_status = "assessed_level_unresolved"
        guidance = ("The assessed level remains unresolved. Any parent identity requires its own "
                    "review; do not apply a catalog fallback label automatically.")
    else:
        suggested_label = None
        decision_status = "rule_not_applicable"
        guidance = ("This rule is outside the supplied scope and suggests no biological label. "
                    "Select an applicable rule for a new review.")
    parent_review = {
        "required_panel_id": rule["parent"]["panel_id"] if rule["parent"] else None,
        "same_unit_high_record_documented": bool(rule["parent"] and parent_ok),
        "supplied_record": evidence.get("parent_evidence") if rule["parent"] else None,
        "retained_as_suggested_label": False,
        "biological_truth_verified_by_tool": False,
        "requires_reassessment_before_reuse": bool(rule["parent"] and
            (not parent_ok or failed_gate or failed_check or strong_conflict or mismatch)),
    }

    ledger = {}
    for key in ("donor_replication", "independent_validation"):
        item = evidence.get(key, {"status": "unknown", "evidence_refs": []})
        _require(isinstance(item, dict) and _text(item.get("status")), f"Invalid {key} ledger")
        warnings = []
        if item["status"] != "unknown" and not _refs(item.get("evidence_refs")):
            warnings.append("claimed_status_without_evidence_references")
        if key == "independent_validation" and item["status"] != "unknown":
            if item.get("held_out_from_annotation") is not True or not _text(item.get("evidence_family")):
                warnings.append("independence_not_documented")
        ledger[key] = {"supplied_record": item, "used_for_review_grade": False,
                       "independence_verified_by_tool": False, "warnings": warnings}
    return {
        "rulebook_version": RULEBOOK_VERSION,
        "rule_id": rule["id"], "unit_type": unit_type, "unit_id": unit_id,
        "target_label": rule["target_label"], "level": rule["level"],
        "target_label_role": "assessed_rule_target_not_an_assigned_label",
        "claim_kind": rule["claim_kind"], "review_grade": grade,
        "review_grade_meaning": ("Human-review completeness, not identity confidence or probability. "
                                 "Moderate with an incomplete core does not establish a type-specific candidate."),
        "candidate_only": True if grade == "Moderate" else False if grade == "High" else None,
        "type_specific_candidate": grade == "Moderate" and complete_core,
        "partial_core_not_type_specific": bool(some_core and not complete_core),
        "decision_status": decision_status,
        "suggested_review_label": suggested_label,
        "reviewer": evidence.get("reviewer", ""), "review_date": evidence.get("review_date", ""),
        "reviewer_identity_verified_by_tool": False,
        "parent_review": parent_review,
        "reasons": reasons, "core_routes": routes,
        "ignored_supported_gene_evidence": ignored_genes,
        "supporting_genes_observed": sorted(usable_genes & set(rule["supporting"]["genes"])),
        "supporting_genes_replace_core": False,
        "rescue_routes_used": [], "separate_evidence_ledgers": ledger,
        "biological_classifier_validated": False, "rule_validation_status": rule["validation_status"],
        "writes_cell_labels": False,
        "interpretation": ("Review-grade completeness, not a calibrated probability or independently "
                           "verified biological identity. Program results establish only a reviewed "
                           "expression program; they do not establish a cell identity or disease effect."),
        "review_guidance": guidance,
        "fallback_guidance": None if grade == "High" else guidance,
        "rule_specific_fallback_guidance": ({"text": rule["fallback"]["missing_core"],
            "use": "Human review only; this text does not assign a target or parent label."}
            if some_core and not complete_core else None),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--validate", action="store_true", help="Check structure/source coverage only")
    action.add_argument("--template", metavar="RULE_ID", help="Print an incomplete manual-review template")
    action.add_argument("--evidence", type=Path, metavar="FILE", help="Review JSON record(s), read-only")
    parser.add_argument("--root", type=Path, default=ROOT, help="Skill package root")
    args = parser.parse_args(argv)
    rules = load_rules(args.root)
    result = validate_rules(args.root, rules=rules)
    by_id = {r["id"]: r for r in rules}
    if args.template:
        _require(args.template in by_id, "Unknown rule ID: " + args.template)
        result = evidence_template(by_id[args.template])
    elif args.evidence:
        raw = json.loads(args.evidence.read_text(encoding="utf-8-sig"))
        records = raw.get("reviews") if isinstance(raw, dict) and "reviews" in raw else raw
        records = [records] if isinstance(records, dict) else records
        _require(isinstance(records, list) and bool(records), "Expected an evidence record or nonempty array")
        outputs = []
        for entry in records:
            _require(isinstance(entry, dict) and entry.get("rule_id") in by_id,
                     "Unknown or missing evidence rule_id")
            outputs.append(review_evidence(by_id[entry["rule_id"]], entry))
        result = {"rulebook_version": RULEBOOK_VERSION, "reviews": outputs,
                  "input_modified": False, "writes_cell_labels": False,
                  "biological_classifier_validated": False}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit("Review error: " + str(exc)) from exc
