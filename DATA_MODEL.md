# Data Model and Geographic Anchors — v0.1

## Design goals
The model is jurisdiction-aware, source-first, multilingual, versioned, interoperable, and simple enough for GitHub pull requests. The machine-readable contracts are the [jurisdiction-node JSON Schema](schemas/jurisdiction-node.v0.1.schema.json) and [geographic-anchor JSON Schema](schemas/geographic-anchor.v0.1.schema.json).

## Keep five concepts separate

### Geographic anchor
A physical discovery point or named site: state capitol, national capitol, parliament, courthouse, judicial center, city hall, airport, seaport, border crossing, library, university, or community archive. An anchor is not a jurisdiction and may be associated with several jurisdictions.

### Institution
A government body or civic organization that exercises a defined function: legislature, court, executive office, election authority, regulator, records office, public library, or archive. Institutions are not interchangeable with their buildings. Several institutions may share a campus; one institution may occupy multiple sites.

### Site catalog
A record about a particular physical site and its public-facing functions, official information, access policies, and relevant rule collections. Visitor guidance and building policies must not automatically be classified as statutes or regulations. Where an enforceable legal instrument exists, create a separate legal-source record.

### Jurisdiction
A legal authority or scope: country, state, province, territory, tribal nation, county, municipality, or supranational organization. Use stable identifiers and explicit parent/relationship metadata where appropriate. A jurisdiction's legal scope is not determined by the location of its capitol, courthouse, or agency office.

### Legal source
A constitution, statute, regulation, bill, court opinion, treaty, gazette notice, or administrative decision. Record issuing authority, canonical URL, publication date, effective date, status, language, and verification date.

### Public-interest record
Journalism, public testimony, community observation, research, or reform proposal. These are not laws and must never be displayed as official legal instruments.

## Civic anchor categories
The v0.1 anchor contract includes:
- Legislative: state capitol, national capitol, parliament.
- Judicial: courthouse, judicial center.
- Municipal: city hall.
- Geographic gateway: airport, seaport, border crossing.
- Knowledge and public memory: library, university, community archive.
- Sovereign and other civic institutions: tribal government, other.

Add new controlled categories only when a real data need appears. Prefer a generic institution record over inventing a new physical anchor for every office inside the same building.

## Relationship rules
1. Every anchor references one or more existing jurisdiction IDs.
2. Every site catalog references an existing anchor ID and existing jurisdiction IDs.
3. An anchor ID must be unique across all anchor collections.
4. Jurisdiction parent IDs must resolve to an existing jurisdiction record.
5. Physical proximity never establishes legal applicability.
6. An institution may be associated with multiple sites; a site may host multiple institutions.
7. Record the source and verification date for addresses, coordinates, and institutional facts.
8. Coordinates use WGS84 decimal degrees and require a source and verification date. Leave coordinates null until verified.

## Required source metadata
Each legal source should have a unique ID, source-language title, jurisdiction ID, issuing authority, document type, canonical URL, language tag, publication/adoption date, effective date, current status, status-as-of date, last-checked date, provenance notes, and review state. Use explicit unknown or pending values; never invent dates or status.

## Geographic identifiers
Prefer authoritative identifiers where available: ISO 3166-1 / ISO 3166-2 for countries and subdivisions; ICAO and IATA for airports; UN M49 for statistical grouping. Wikidata or GeoNames may supplement discovery but are not legal authority. Never infer legal boundaries from a point.

## Versioning and correction
Do not silently replace a legal version or public contribution. Add a new record referencing the prior record with a relationship such as supersedes, amends, repeals, or corrects. A correction to an Atlas record corrects the Atlas representation; it does not amend the law.

## Translation
Preserve source-language text and URL. Each translation is separate and records target language, translator or method, date/version, review state, and whether it is official, human-reviewed, or machine-unreviewed. Machine translations must not be presented as official.

## Integrity and privacy
Future records may include digests, algorithms, timestamps, and signing-key identifiers. Never place sensitive source identities or private information in a permanent public log. Hashes are integrity references, not proof of truth or authority. Do not publish private correspondence, credentials, confidential legal advice, or identifying details about vulnerable sources.

## Colorado pilot coverage
Begin with the Colorado Constitution, Colorado Revised Statutes, session laws and enrolled acts, appellate opinions, Code of Colorado Regulations, legislative bills and histories, relevant federal sources, municipal charters and codes, and tribal legal authorities where appropriate and with respect for each sovereign's own publication rules. This is a starter index, not exhaustive coverage.
