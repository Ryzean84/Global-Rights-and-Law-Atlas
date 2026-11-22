# Data Model and Geographic Anchors — v0.2

## Design goals
The model is jurisdiction-aware, source-first, multilingual, versioned, interoperable, and simple enough for GitHub pull requests. Machine-readable contracts are provided for [jurisdictions](schemas/jurisdiction-node.v0.1.schema.json), [geographic anchors](schemas/geographic-anchor.v0.1.schema.json), [institutions](schemas/institution.v0.1.schema.json), and [site catalogs](schemas/site-catalog.v0.1.schema.json), [legal sources](schemas/legal-source.v0.2.schema.json), [oversight records](schemas/oversight-record.v0.3.schema.json), and [government AI systems](schemas/government-ai-system.v0.3.schema.json).

## Keep six concepts separate

### Geographic anchor
A physical discovery point or named site: state capitol, national capitol, parliament, courthouse, judicial center, city hall, airport, seaport, border crossing, library, university, or community archive. An anchor is not a jurisdiction and may be associated with several jurisdictions.

### Institution
A government body or civic organization that exercises a defined function: legislature, legislative chamber, court, executive office, election authority, regulator, records office, public library, or archive. Institutions are not interchangeable with their buildings. Several institutions may share a campus; one institution may occupy multiple sites. Each institution has a stable ID, type, jurisdiction links, site links, authoritative source URLs, and a verification date.

### Site catalog
A record about a particular physical site and its public-facing functions, official information, access policies, and relevant rule collections. Site catalogs link to institution IDs, but visitor guidance and building policies must not automatically be classified as statutes or regulations. Where an enforceable legal instrument exists, create a separate legal-source record.

### Jurisdiction
A legal authority or scope: country, state, province, territory, tribal nation, county, municipality, or supranational organization. Use stable identifiers and explicit parent/relationship metadata where appropriate. A jurisdiction's legal scope is not determined by the location of its capitol, courthouse, or agency office.

### Legal source
A constitution, statute, regulation, bill, court opinion, treaty, gazette notice, or administrative decision. Record issuing authority, canonical URL, publication date, effective date, status, language, and verification date.

### Legal-source collection record
A collection-level pointer to an official portal or publication series. It records source type, issuing/publishing authority, legal-effect category, canonical URL, language, dates when known, collection status, institutions associated with the publisher or issuing body, verification state, and provenance notes. A collection pointer does not establish that every item within it is current, binding, or correctly interpreted. Individual laws, regulations, and opinions require their own records with instrument-level dates, identifiers, status, and history. For example, the Colorado pilot includes the enacted 2026 SB26-189 and HB26-1263 acts, with their distinct overall effective dates and delayed applicability for selected duties. Never collapse an act's overall effective date into the application date of every provision.

### Oversight and accountability record
A traceable public record of an audit, rulemaking, enforcement action, investigation, implementation deadline, or public response. It links the responsible institution, affected or reviewed institutions, jurisdiction, legal-source records, evidence URLs, status date, and evidence grade. Distinguish primary-source facts from secondary-reported developments. An audit listing is not a substitute for reading the report, and an audit record must not imply findings that have not been extracted and reviewed. Confidential workpapers and unreleased reports are out of scope.

### Government AI system inventory record
A record of a specific AI system used, procured, piloted, or formally planned by a public institution. Capture owner and operator separately, deployment status, purpose, decision domains, affected populations, human oversight, public notices, procurement evidence, legal authorities, and oversight links. Do not create a system record from speculation, generic vendor marketing, or an agency's use of ordinary software. An empty inventory is an explicit evidence gap, not proof that no systems exist.

### Public-interest record
Journalism, public testimony, community observation, research, or reform proposal. These are not laws and must never be displayed as official legal instruments.

## Civic anchor categories
The v0.1 anchor contract includes:
- Legislative: state capitol, national capitol, parliament.
- Judicial: courthouse, judicial center.
- Municipal: city hall.
- Executive and civic services: government office.
- Geographic gateway: airport, seaport, border crossing.
- Knowledge and public memory: library, university, community archive.
- Sovereign and other civic institutions: tribal government, other.

Institution categories are separately controlled in the institution schema. Prefer a generic institution record over inventing a new physical anchor for every office inside the same building.

## Relationship rules
1. Every anchor references one or more existing jurisdiction IDs.
2. Every site catalog references an existing anchor ID and existing jurisdiction IDs.
3. Every institution references one or more existing jurisdictions and one or more existing sites.
4. Site-to-institution and institution-to-site links must agree in both directions.
5. Anchor, site, jurisdiction, and institution IDs must be unique within their respective registries.
6. Jurisdiction parent IDs must resolve to an existing jurisdiction record.
7. Physical proximity never establishes legal applicability.
8. Record the source and verification date for addresses, coordinates, and institutional facts.
9. Coordinates use WGS84 decimal degrees and require a source and verification date. Leave coordinates null until verified.
10. Every legal-source record must resolve to an existing jurisdiction; optional institution links must resolve to existing institution IDs.
11. Collection-level portals and individual legal instruments are different record granularities and must not be conflated.
12. A bill, resolution, enrolled act, codified statute, administrative rule, slip opinion, and audit report have different legal or evidentiary roles.
13. Oversight records must identify their evidence grade and the date on which status was checked.
14. Government AI inventory entries require public evidence and a named owner institution; unverified leads remain separate from confirmed deployments.
15. Absence of a public record is not evidence that an audit, AI deployment, investigation, or enforcement action does not exist.

## Required source metadata
Each legal-source record should have a unique ID, source-language title, jurisdiction ID, issuing/publishing authority, source type, legal-effect category, canonical URL, language tag, publication date when known, effective date when applicable, collection status, status-as-of date, last-checked date, linked institution IDs where appropriate, provenance notes, and review state. Use explicit null or unknown values; never invent dates or legal status. The v0.2 contract and Colorado portal collection are in [the legal-source schema](schemas/legal-source.v0.2.schema.json) and [Colorado official legal-source registry](data/legal-sources/colorado-official-portals.json).

## Geographic identifiers
Prefer authoritative identifiers where available: ISO 3166-1 / ISO 3166-2 for countries and subdivisions; ICAO and IATA for airports; UN M49 for statistical grouping. Wikidata or GeoNames may supplement discovery but are not legal authority. Never infer legal boundaries from a point.

## Versioning and correction
Do not silently replace a legal version or public contribution. Add a new record referencing the prior record with a relationship such as supersedes, amends, repeals, or corrects. A correction to an Atlas record corrects the Atlas representation; it does not amend the law.

## Translation
Preserve source-language text and URL. Each translation is separate and records target language, translator or method, date/version, review state, and whether it is official, human-reviewed, or machine-unreviewed. Machine translations must not be presented as official.

## Integrity and privacy
Future records may include digests, algorithms, timestamps, and signing-key identifiers. Never place sensitive source identities or private information in a permanent public log. Hashes are integrity references, not proof of truth or authority. Do not publish private correspondence, credentials, confidential legal advice, or identifying details about vulnerable sources.

## Colorado pilot coverage
Begin with the Colorado Constitution, Colorado Revised Statutes, session laws and enrolled acts, appellate opinions, Code of Colorado Regulations, legislative bills and histories, relevant federal sources, municipal charters and codes, and tribal legal authorities where appropriate and with respect for each sovereign's own publication rules. The first legal-source collection indexes official portals for the Colorado Constitution, CRS, session laws, CCR, appellate opinions, legislative records, and public State Auditor reports. The accountability layer adds a public IT audit record and a carefully qualified 4 CCR 904-6 rulemaking tracker. The initial Colorado government AI inventory is intentionally empty until specific deployments are supported by public evidence. This is a starter index, not exhaustive coverage.
