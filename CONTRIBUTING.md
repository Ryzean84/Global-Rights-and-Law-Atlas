# Contributing to the Atlas

You do not need to know how to build a website to contribute. The first contribution path is a GitHub pull request containing structured data and source links.

## Good first contributions
- Add an official legal-source URL for a jurisdiction.
- Verify a publication date, effective date, amendment, or repeal.
- Add a geographic discovery anchor with an authoritative identifier.
- Add a reviewed translation or translation metadata.
- Improve accessibility, documentation, or source-language keywords.
- Submit a clearly labeled journalism or community resource with appropriate permissions and privacy safeguards.

## Workflow
1. Fork this repository.
2. Choose an existing jurisdiction or propose a new one.
3. Add or edit a JSON record using the schema.
4. Include authoritative sources and dates; explain uncertainty.
5. Validate the JSON if possible.
6. Open a pull request using the repository template.
7. Respond to review questions about authority, status, privacy, rights, or context.

If you cannot use Git locally, GitHub's web interface can create or edit a file and open a pull request.

## Source hierarchy
Prefer official gazettes and authenticated publications, legislatures/parliaments, courts/judiciaries, regulators, treaty depositaries, then reputable secondary sources for context. A source may be official but outdated. Check amendments, repeal, commencement, and current status.

## Suggested review states
- draft
- source_checked
- status_checked
- needs_review
- superseded
- withdrawn

A pull request merge is not court certification and does not make an interpretation authoritative.

## Corrections and disagreements
Point to the exact source, passage, date, or field. Preserve competing interpretations when appropriate and label them. If a record creates privacy or safety risk, contact maintainers for a safe restriction process instead of reposting sensitive material.

## Safety
Do not submit doxxing, threats, harassment, calls for violence, credentials, confidential communications, private source identities, or instructions for evading legal obligations. The Atlas supports lawful research, journalism, public education, peaceful advocacy, and rights awareness.

Use the pull request template in .github/PULL_REQUEST_TEMPLATE.md.
