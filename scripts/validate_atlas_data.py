#!/usr/bin/env python3
"""Validate Atlas jurisdiction, anchor, and site registries.

Checks JSON syntax, JSON Schema contracts, stable IDs, and cross-registry
references. Geographic anchors remain distinct from legal jurisdictions.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMAS = ROOT / "schemas"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {exc}")
        return None


errors: list[str] = []


def report(message: str) -> None:
    errors.append(message)


def validate_schema(instance, schema, path: Path) -> bool:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    found = sorted(validator.iter_errors(instance), key=lambda err: (list(map(str, err.path)), err.message))
    for err in found:
        location = ".".join(str(part) for part in err.path) or "<root>"
        report(f"{path.relative_to(ROOT)}:{location}: {err.message}")
    return not found


def main() -> int:
    jurisdiction_schema_path = SCHEMAS / "jurisdiction-node.v0.1.schema.json"
    anchor_schema_path = SCHEMAS / "geographic-anchor.v0.1.schema.json"
    jurisdiction_schema = load_json(jurisdiction_schema_path)
    anchor_schema = load_json(anchor_schema_path)
    if jurisdiction_schema is None or anchor_schema is None:
        return 1

    try:
        Draft202012Validator.check_schema(jurisdiction_schema)
        Draft202012Validator.check_schema(anchor_schema)
    except Exception as exc:  # schema errors should fail CI with a useful message
        report(f"Invalid JSON Schema: {exc}")
        return 1

    jurisdiction_files = sorted((DATA / "jurisdictions").rglob("*.json"))
    if not jurisdiction_files:
        report("data/jurisdictions: no jurisdiction records found")

    jurisdictions: dict[str, Path] = {}
    for path in jurisdiction_files:
        record = load_json(path)
        if record is None:
            continue
        validate_schema(record, jurisdiction_schema, path)
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in jurisdictions:
                report(f"{path.relative_to(ROOT)}: duplicate jurisdiction id {record_id} (also in {jurisdictions[record_id].relative_to(ROOT)})")
            else:
                jurisdictions[record_id] = path

    for path in jurisdiction_files:
        record = load_json(path)
        if not isinstance(record, dict):
            continue
        parent_id = record.get("parent_jurisdiction_id")
        if parent_id and parent_id not in jurisdictions:
            report(f"{path.relative_to(ROOT)}: unknown parent_jurisdiction_id {parent_id}")

    anchor_files = sorted((DATA / "anchors").rglob("*.json"))
    anchors: dict[str, Path] = {}
    for path in anchor_files:
        payload = load_json(path)
        if not isinstance(payload, dict):
            continue
        if payload.get("schema_version") != "0.1.0":
            report(f"{path.relative_to(ROOT)}: schema_version must be 0.1.0")
        if not isinstance(payload.get("collection_id"), str) or not payload["collection_id"]:
            report(f"{path.relative_to(ROOT)}: collection_id is required")
        records = payload.get("anchors")
        if not isinstance(records, list):
            report(f"{path.relative_to(ROOT)}: anchors must be an array")
            continue
        for index, anchor in enumerate(records):
            if not isinstance(anchor, dict):
                report(f"{path.relative_to(ROOT)}: anchors[{index}] must be an object")
                continue
            validate_schema(anchor, anchor_schema, path)
            anchor_id = anchor.get("id")
            if isinstance(anchor_id, str):
                if anchor_id in anchors:
                    report(f"{path.relative_to(ROOT)}: duplicate anchor id {anchor_id} (also in {anchors[anchor_id].relative_to(ROOT)})")
                else:
                    anchors[anchor_id] = path
            for jurisdiction_id in anchor.get("jurisdiction_ids", []):
                if jurisdiction_id not in jurisdictions:
                    report(f"{path.relative_to(ROOT)}: anchor {anchor_id} references unknown jurisdiction {jurisdiction_id}")

    site_files = sorted((DATA / "sites").rglob("*.json"))
    for path in site_files:
        site = load_json(path)
        if not isinstance(site, dict):
            continue
        for field in ("site_id", "anchor_id", "name", "jurisdiction_ids"):
            if field not in site:
                report(f"{path.relative_to(ROOT)}: missing required site field {field}")
        anchor_id = site.get("anchor_id")
        if anchor_id and anchor_id not in anchors:
            report(f"{path.relative_to(ROOT)}: unknown anchor_id {anchor_id}")
        for jurisdiction_id in site.get("jurisdiction_ids", []):
            if jurisdiction_id not in jurisdictions:
                report(f"{path.relative_to(ROOT)}: site {site.get('site_id')} references unknown jurisdiction {jurisdiction_id}")

    if errors:
        print("\n".join(f"ERROR: {message}" for message in errors))
        print(f"Atlas validation failed with {len(errors)} error(s).")
        return 1

    print(f"VALID: {len(jurisdictions)} jurisdiction record(s)")
    print(f"VALID: {len(anchors)} unique geographic anchor(s) across {len(anchor_files)} collection(s)")
    print(f"VALID: {len(site_files)} site catalog(s), with all anchor and jurisdiction references resolved")
    print("Atlas data validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
