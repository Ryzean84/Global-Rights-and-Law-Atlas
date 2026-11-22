# Data Model and Geographic Anchors — v0.1

## Design goals
The model is jurisdiction-aware, source-first, multilingual, versioned, interoperable, and simple enough for GitHub pull requests. The machine-readable contract is [the jurisdiction-node JSON Schema](schemas/jurisdiction-node.v0.1.schema.json).

## Keep four concepts separate
### Geographic anchor
A discovery point or named area: airport, seaport, town, courthouse, library, university, border crossing, or community archive. An anchor is not a jurisdiction and may be associated with several jurisdictions.

### Jurisdiction
A legal authority or scope: country, state, province, territory, tribal nation, municipality, or supranational organization. Use stable identifiers and explicit parent/relationship metadata where appropriate.

### Legal source
A constitution, statute, regulation, bill, court opinion, treaty, gazette notice, or administrative decision. Record issuing authority, canonical URL, publication date, effective date, status, language, and verification date.

### Public-interest record
Journalism, public testimony, community observation, research, or reform proposal. These are not laws and must never be displayed as official legal instruments.

## Required source metadata
Each legal source should have a unique ID, source-language title, jurisdiction ID, issuing authority, document type, canonical URL, language tag, publication/adoption date, effective date, current status, status-as-of date, last-checked date, provenance notes, and review state. Use explicit unknown or pending values; never invent dates or status.

## Geographic identifiers
Prefer authoritative identifiers where available: ISO 3166-1 / ISO 3166-2 for countries and subdivisions; ICAO and IATA for airports; UN M49 for statistical grouping. Wikidata or GeoNames may supplement discovery but are not legal authority. Coordinates use WGS84 decimal degrees and require a source and verification date. Never infer legal boundaries from a point.

## Versioning and correction
Do not silently replace a legal version or public contribution. Add a new record referencing the prior record with a relationship such as supersedes, amends, repeals, or corrects. A correction to an Atlas record corrects the Atlas representation; it does not amend the law.

## Translation
Preserve source-language text and URL. Each translation is separate and records target language, translator or method, date/version, review state, and whether it is official, human-reviewed, or machine-unreviewed. Machine translations must not be presented as official.

## Integrity and privacy
Future records may include digests, algorithms, timestamps, and signing-key identifiers. Never place sensitive source identities or private information in a permanent public log. Hashes are integrity references, not proof of truth or authority. Do not publish private correspondence, credentials, confidential legal advice, or identifying details about vulnerable sources.

## Colorado pilot coverage
Begin with the Colorado Constitution, Colorado Revised Statutes, session laws and enrolled acts, appellate opinions, Code of Colorado Regulations, legislative bills and histories, relevant federal sources, and tribal legal authorities where appropriate and with respect for each sovereign's own publication rules. This is a starter index, not exhaustive coverage.
