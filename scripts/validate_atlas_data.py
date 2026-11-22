#!/usr/bin/env python3
"""Validate Atlas jurisdiction, anchor, site, institution, and legal-source registries."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMAS = ROOT / "schemas"
errors: list[str] = []


def report(message: str) -> None:
    errors.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {exc}")
        return None


def validate_schema(instance, schema, path: Path) -> bool:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    found = sorted(validator.iter_errors(instance), key=lambda err: (list(map(str, err.path)), err.message))
    for err in found:
        location = ".".join(str(part) for part in err.path) or "<root>"
        report(f"{path.relative_to(ROOT)}:{location}: {err.message}")
    return not found


def main() -> int:
    schema_names = {
        "jurisdiction": "jurisdiction-node.v0.1.schema.json",
        "anchor": "geographic-anchor.v0.1.schema.json",
        "institution": "institution.v0.1.schema.json",
        "site": "site-catalog.v0.1.schema.json",
        "legal_source": "legal-source.v0.2.schema.json",
    }
    schemas = {}
    for kind, filename in schema_names.items():
        path = SCHEMAS / filename
        schema = load_json(path)
        if schema is None:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            report(f"{path.relative_to(ROOT)}: invalid JSON Schema: {exc}")
        schemas[kind] = schema
    if len(schemas) != len(schema_names):
        return 1

    jurisdiction_files = sorted((DATA / "jurisdictions").rglob("*.json"))
    jurisdictions: dict[str, Path] = {}
    for path in jurisdiction_files:
        record = load_json(path)
        if not isinstance(record, dict):
            continue
        validate_schema(record, schemas["jurisdiction"], path)
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in jurisdictions:
                report(f"{path.relative_to(ROOT)}: duplicate jurisdiction id {record_id} (also in {jurisdictions[record_id].relative_to(ROOT)})")
            else:
                jurisdictions[record_id] = path
    if not jurisdiction_files:
        report("data/jurisdictions: no jurisdiction records found")

    for path in jurisdiction_files:
        record = load_json(path)
        if isinstance(record, dict):
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
            validate_schema(anchor, schemas["anchor"], path)
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
    sites: dict[str, tuple[Path, dict]] = {}
    for path in site_files:
        site = load_json(path)
        if not isinstance(site, dict):
            continue
        validate_schema(site, schemas["site"], path)
        site_id = site.get("site_id")
        if isinstance(site_id, str):
            if site_id in sites:
                report(f"{path.relative_to(ROOT)}: duplicate site id {site_id} (also in {sites[site_id][0].relative_to(ROOT)})")
            else:
                sites[site_id] = (path, site)
        anchor_id = site.get("anchor_id")
        if anchor_id and anchor_id not in anchors:
            report(f"{path.relative_to(ROOT)}: unknown anchor_id {anchor_id}")
        for jurisdiction_id in site.get("jurisdiction_ids", []):
            if jurisdiction_id not in jurisdictions:
                report(f"{path.relative_to(ROOT)}: site {site_id} references unknown jurisdiction {jurisdiction_id}")

    institution_files = sorted((DATA / "institutions").rglob("*.json"))
    institutions: dict[str, tuple[Path, dict]] = {}
    for path in institution_files:
        payload = load_json(path)
        if not isinstance(payload, dict):
            continue
        if payload.get("schema_version") != "0.1.0":
            report(f"{path.relative_to(ROOT)}: schema_version must be 0.1.0")
        if not isinstance(payload.get("collection_id"), str) or not payload["collection_id"]:
            report(f"{path.relative_to(ROOT)}: collection_id is required")
        records = payload.get("institutions")
        if not isinstance(records, list):
            report(f"{path.relative_to(ROOT)}: institutions must be an array")
            continue
        for index, institution in enumerate(records):
            if not isinstance(institution, dict):
                report(f"{path.relative_to(ROOT)}: institutions[{index}] must be an object")
                continue
            validate_schema(institution, schemas["institution"], path)
            institution_id = institution.get("id")
            if isinstance(institution_id, str):
                if institution_id in institutions:
                    report(f"{path.relative_to(ROOT)}: duplicate institution id {institution_id} (also in {institutions[institution_id][0].relative_to(ROOT)})")
                else:
                    institutions[institution_id] = (path, institution)
            for jurisdiction_id in institution.get("jurisdiction_ids", []):
                if jurisdiction_id not in jurisdictions:
                    report(f"{path.relative_to(ROOT)}: institution {institution_id} references unknown jurisdiction {jurisdiction_id}")
            for site_id in institution.get("site_ids", []):
                if site_id not in sites:
                    report(f"{path.relative_to(ROOT)}: institution {institution_id} references unknown site {site_id}")
                elif institution_id not in sites[site_id][1].get("institution_ids", []):
                    report(f"{path.relative_to(ROOT)}: institution {institution_id} lists site {site_id}, but the site does not list the institution")

    for site_id, (path, site) in sites.items():
        for institution_id in site.get("institution_ids", []):
            if institution_id not in institutions:
                report(f"{path.relative_to(ROOT)}: site {site_id} references unknown institution {institution_id}")
            elif site_id not in institutions[institution_id][1].get("site_ids", []):
                report(f"{path.relative_to(ROOT)}: site {site_id} lists institution {institution_id}, but the institution does not list the site")

    if errors:
        print("\n".join(f"ERROR: {message}" for message in errors))
        print(f"Atlas validation failed with {len(errors)} error(s).")
        return 1

    print(f"VALID: {len(jurisdictions)} jurisdiction record(s)")
    print(f"VALID: {len(anchors)} unique geographic anchor(s) across {len(anchor_files)} collection(s)")
    print(f"VALID: {len(sites)} site catalog(s)")
    print(f"VALID: {len(institutions)} unique institution record(s) across {len(institution_files)} collection(s)")
    print(f"VALID: {len(legal_sources)} unique legal-source record(s) across {len(legal_source_files)} collection(s)")
    print("All schema, uniqueness, parent, and cross-registry reference checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
