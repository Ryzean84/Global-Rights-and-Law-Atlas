# Civic Anchor Expansion Roadmap

## Purpose

Build a source-linked geographic index of civic institutions and the jurisdictions they serve. The Atlas should help people discover where public authority is exercised, which institutions operate at a site, and where authoritative legal materials can be found.

A map pin is a discovery aid, not a legal conclusion. Physical proximity never establishes the scope of a law or the authority of an institution.

## Expansion sequence

### Phase 0 — Colorado foundation
**Status: implemented in the current pilot branch; pending final review and merge.**

- Colorado State Capitol and its legislative / executive institutions
- Ralph L. Carr Colorado Judicial Center
- Denver City and County Building
- Colorado Secretary of State office
- Colorado Office of the State Auditor (independent, nonpartisan Legislative Branch agency)
- Denver International Airport as a geographic gateway
- United States, Colorado, and Denver starter jurisdiction records
- Versioned jurisdiction, anchor, and institution contracts
- Automated uniqueness and cross-reference validation

### Phase 1 — Complete Colorado's statewide civic skeleton
Add and verify:
- Colorado Governor's Residence only if it provides a meaningful public-facing civic function or authoritative source collection
- Colorado's remaining statewide elected offices and major agencies at their actual office sites
- State archives and law libraries
- County courthouses and county government centers
- Municipal halls and city / town clerk offices
- Water courts and other specialized courts where their distinct jurisdiction or public access makes them useful
- Tribal legal and archival sources only through sovereign-specific official sources and respectful, informed engagement

Do not create a separate anchor for every office in a shared building. Reuse the site anchor and create distinct institution records.

### Phase 2 — Fifty-state capitol network
For each state, begin with a consistent minimum set:
1. State capitol building / legislature site
2. Legislature as an institution, with chambers where useful
3. Governor's office
4. State supreme court or highest court
5. Secretary of State / election authority
6. Attorney General / state legal office
7. Official state legal-source portal

Each record must be independently sourced from the relevant state's official legislature, judiciary, agency, or records authority. Do not copy one state's structure into another without checking its constitutional arrangements.

### Phase 3 — United States federal civic network
Potential anchors and institutions:
- United States Capitol and Congress
- Supreme Court of the United States
- White House and Executive Office of the President
- National Archives and Records Administration
- Library of Congress
- Federal Register / Government Publishing Office
- Federal departments, agencies, and independent commissions

Federal jurisdiction must remain distinct from state, territorial, tribal, and municipal jurisdiction records.

### Phase 4 — Territories, tribal nations, and distinct political jurisdictions
Represent each jurisdiction according to its own constitutional and legal status. Do not flatten tribal nations into counties, municipalities, or ordinary state subdivisions. Parent-child relationships in the current v0.1 model are not sufficient to express every sovereignty, treaty, federal relationship, or jurisdictional overlap; richer relationship types may be required before broad ingestion.

### Phase 5 — International civic network
Expand through:
- National capitols and parliaments
- Constitutional and supreme courts
- Ministries and national agencies
- Official gazettes and national archives
- Regional and local government institutions
- International airports, seaports, and border crossings as discovery gateways

Preserve each jurisdiction's official language, original legal text, local source conventions, and institutional structure. Do not rank legal systems or presume that one country's constitutional arrangement is universal.

## Data acceptance gate

Before an anchor, site, institution, or legal source is accepted:

- Use an authoritative source from the institution or responsible government.
- Identify the issuing authority and relevant jurisdiction IDs explicitly.
- Keep the physical anchor, institution, jurisdiction, site policy, and legal instrument as separate concepts.
- Record a source URL and verification date.
- Leave coordinates null until verified from an authoritative source.
- Do not label visitor guidance or a website summary as binding law.
- Record uncertainty and known gaps instead of filling them with guesses.
- Ensure all IDs and cross-registry references pass automated validation.
- Review privacy, safety, accessibility, language, and sovereign/community context.

## Milestone definition

A region is ready to expand beyond its pilot when:
- Its primary civic institutions have stable IDs and authoritative source links.
- Physical sites link to institutions, and institutions link back to sites.
- Jurisdiction records resolve without inferred boundaries.
- The relevant legal-source portals are identified.
- The data validator passes on the exact proposed commit.
- Known omissions are documented.

The Atlas should grow by verified coverage, not by pin count.
