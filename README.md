# Global Rights and Law Atlas

**We the People, not We the Corporation.**

An open-source, multilingual, federated civic atlas connecting laws, founding documents, human-rights protections, digital rights, journalism, and the voices of the communities affected by them.

The Atlas makes primary sources and their histories easier to discover, compare, translate, cite, and improve. It does not issue legal advice, determine whether a law is just, rank countries, or replace courts, lawyers, journalists, or local institutions.

## Start here
- [Project charter](CHARTER.md)
- [Data and geographic anchor model](DATA_MODEL.md)
- [Contributing guide](CONTRIBUTING.md)
- [Colorado pilot jurisdiction record](data/jurisdictions/us-co.json)
- [Airport gateway anchor registry](data/anchors/airport-gateways.json)
- [Jurisdiction-node JSON Schema](schemas/jurisdiction-node.v0.1.schema.json)

## First pilot: Colorado
The first source registry points to official materials for the Colorado Constitution, Colorado Revised Statutes, session laws, appellate opinions, and executive agency rules. It also identifies Colorado's 2026 automated decision-making legislation as a changing legal record whose bill history, enacted text, effective date, and rulemaking context must be retained.

Starter records are discovery pointers, not a complete or independently certified legal collection. Verify current status against authoritative sources before describing a provision as current law.

## Geographic discovery: gateways, not borders
International airports are useful discovery anchors, not legal jurisdictions. Every anchor must point to separately identified jurisdictions; legal coverage must never be inferred from proximity alone. The network can expand to cities, towns, counties, states, provinces, tribal nations, islands, courts, universities, libraries, and community archives.

## How contributions work
1. Choose or propose a geographic anchor and identify the jurisdiction.
2. Add authoritative legal sources with authority, document type, dates, status, language, and URL.
3. Preserve original-language material and record translations separately.
4. Submit the structured contribution as a GitHub pull request.
5. Automated checks validate structure; people review authority, accuracy, rights, privacy, and context.
6. Accepted changes are versioned. Corrections and superseding laws are recorded as new history, not silently overwritten.

## Integrity without pretending to prove truth
Git history, checksums, signatures, append-only event records, Merkle roots, and independent mirrors can make changes detectable. They do not prove a source is truthful, a legal interpretation is correct, a record is complete, or a law is fair. No cryptocurrency or single blockchain is required.

## Current maturity
This repository currently contains foundational documentation, a starter Colorado source registry, an airport gateway anchor record, and a versioned data schema. It is not yet a complete legal database, interactive map, legal-advice service, blockchain, or production federation network.

**Build locally. Connect globally. Preserve independently.**
