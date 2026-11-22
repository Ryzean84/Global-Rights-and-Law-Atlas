# Global Rights and Law Atlas

**We the People, not We the Corporation.**

An open-source, multilingual, federated civic atlas connecting laws, founding documents, human-rights protections, digital rights, journalism, and the voices of the communities affected by them.

The Atlas makes primary sources and their histories easier to discover, compare, translate, cite, and improve. It does not issue legal advice, determine whether a law is just, rank countries, or replace courts, lawyers, journalists, or local institutions.

## Start here
- [Project charter](CHARTER.md)
- [Data and geographic anchor model](DATA_MODEL.md)
- [Civic anchor expansion roadmap](docs/CIVIC_ANCHOR_EXPANSION_ROADMAP.md)
- [Contributing guide](CONTRIBUTING.md)
- [United States jurisdiction record](data/jurisdictions/us.json)
- [Colorado jurisdiction record](data/jurisdictions/us-co.json)
- [Denver municipal jurisdiction record](data/jurisdictions/us-co-denver.json)
- [Airport gateway anchor registry](data/anchors/airport-gateways.json)
- [Colorado civic-site anchors](data/anchors/colorado-civic-sites.json)
- [Colorado State Capitol site catalog](data/sites/colorado-state-capitol.json)
- [Ralph L. Carr Judicial Center site catalog](data/sites/ralph-l-carr-judicial-center.json)
- [Denver City and County Building site catalog](data/sites/denver-city-and-county-building.json)
- [Colorado Secretary of State site catalog](data/sites/colorado-secretary-of-state.json)
- [Colorado Office of the State Auditor site catalog](data/sites/colorado-office-of-state-auditor.json)
- [Denver International Airport site catalog](data/sites/denver-international-airport.json)
- [Colorado state-government institutions](data/institutions/colorado-state-government.json)
- [Colorado judicial and legal institutions](data/institutions/colorado-courts-and-oversight.json)
- [Denver municipal institutions](data/institutions/denver-municipal-government.json)
- [Colorado official legal-source registry](data/legal-sources/colorado-official-portals.json)
- [Legal-source JSON Schema](schemas/legal-source.v0.2.schema.json)
- [Colorado public accountability records](data/oversight/colorado-accountability.json)
- [Oversight-record JSON Schema](schemas/oversight-record.v0.3.schema.json)
- [Colorado government AI inventory](data/government-ai/colorado-state-inventory.json)
- [Government AI system JSON Schema](schemas/government-ai-system.v0.3.schema.json)
- [Geographic-anchor JSON Schema](schemas/geographic-anchor.v0.1.schema.json)
- [Jurisdiction-node JSON Schema](schemas/jurisdiction-node.v0.1.schema.json)
- [Institution JSON Schema](schemas/institution.v0.1.schema.json)
- [Site catalog JSON Schema](schemas/site-catalog.v0.1.schema.json)
- [Atlas data validator](scripts/validate_atlas_data.py)

## First pilot: Colorado
The Colorado legal-source registry indexes seven official publication portals and two individual 2026 enacted AI laws: SB26-189 (Automated Decision-Making Technology, Chapter 131) and HB26-1263 (Conversational Artificial Intelligence Service Operator Requirements, Chapter 208). The accountability layer adds the State Auditor's public Cybersecurity Resiliency IT audit listing and a 4 CCR 904-6 rulemaking tracker whose adoption and filing status is explicitly qualified by its evidence sources. The initial government AI inventory is intentionally empty until individual deployments can be documented from public evidence; this is a research gap, not a claim that no public-sector AI systems exist.

The geographic pilot begins with the Colorado State Capitol, Ralph L. Carr Colorado Judicial Center, Denver City and County Building, and Denver International Airport. Each physical anchor is linked to explicit jurisdiction records and a separate site catalog. First-class institution records identify the government bodies and courts associated with those sites.

Starter records are discovery pointers, not a complete or independently certified legal collection. Verify current status against authoritative sources before describing a provision as current law.

## Geographic discovery: gateways, institutions, and jurisdictions
Capitols, legislatures, courts, city halls, agency offices, airports, ports, border crossings, libraries, and archives can all serve as discovery anchors. A physical anchor is not a legal jurisdiction. One campus may host several institutions, and one institution may operate from several sites. Every anchor, site, and institution must point to separately identified jurisdictions; legal coverage must never be inferred from proximity alone.

## How contributions work
1. Choose or propose a geographic anchor and identify the jurisdiction.
2. Add or update an institution record and link it to one or more site records where appropriate.
3. Add a legal-source collection pointer or individual instrument record with authority, source type, legal effect, dates, status, language, provenance, and URL.
4. Preserve original-language material and record translations separately.
5. Submit the structured contribution as a GitHub pull request.
6. Automated checks validate schemas, identifiers, and bidirectional cross-registry references; people review authority, accuracy, rights, privacy, and context.
7. Accepted changes are versioned. Corrections and superseding laws are recorded as new history, not silently overwritten.

Run the local validator with `python scripts/validate_atlas_data.py` after installing `jsonschema`.

## Integrity without pretending to prove truth
Git history, checksums, signatures, append-only event records, Merkle roots, and independent mirrors can make changes detectable. They do not prove a source is truthful, a legal interpretation is correct, a record is complete, or a law is fair. No cryptocurrency or single blockchain is required.

## Current maturity
This repository contains foundational documentation, starter United States / Colorado / Denver jurisdiction records, six geographic anchors, six site catalogs, fourteen institution records, nine Colorado legal-source records (seven portals and two enacted acts), two oversight records, an evidence-first government AI inventory awaiting verified system entries, versioned JSON Schemas, and automated cross-registry validation. It is not yet a complete legal database, interactive map, legal-advice service, blockchain, or production federation network.

**Build locally. Connect globally. Preserve independently.**
