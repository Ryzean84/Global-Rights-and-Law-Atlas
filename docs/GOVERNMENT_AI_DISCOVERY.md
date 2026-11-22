# Colorado Government AI Discovery — Evidence Notes

**Research checkpoint:** 2026-11-22  
**Scope:** Colorado state agencies; initial public-source inventory  
**Purpose:** Preserve the trail from public evidence to Atlas records without turning an agency-reported inventory into an independent audit.

## Primary sources located

1. **Colorado OIT, “AI Inventory” presented to the Joint Technology Committee, December 16, 2025**  
   https://content.leg.colorado.gov/sites/default/files/2025-12/OIT-AI%20Inventory%20JTC%2012-16-2025.pdf  
   A tabular inventory of agency AI-related tools, with agency, project title, approval status, and phase. The document includes both pre-production and production entries. Its rows are useful discovery evidence, but a product name and production label alone do not establish purpose, model behavior, affected populations, or legal significance.

2. **Colorado OIT, “GenAI Projects by Agency”**  
   https://content.leg.colorado.gov/sites/default/files/2025-12/OIT-GenAI%20Projects.pdf  
   Provides project-level descriptions for selected agency use cases, vendors/models, status, and agency statements about decision-making and human review. It expressly distinguishes generative AI projects from machine learning, agentic AI, and other non-generative AI methods. Its scope is therefore not a complete inventory of every algorithmic system used by Colorado government.

3. **Colorado OIT Artificial Intelligence Guide**  
   https://oit.colorado.gov/  
   OIT's public guide describes a statewide GenAI policy under which GenAI efforts and use cases, including third-party vendor projects, must go through OIT risk assessment. Verify the current canonical guide and policy text before quoting detailed requirements.

4. **Colorado OIT Google Gemini pilot case study**  
   https://oit.colorado.gov/  
   OIT describes a 90-day pilot involving 150 participants across 18 state agencies. The case study is evidence of a cross-agency pilot and evaluation process, not evidence that every participant used the tool for decisions about residents.

5. **Colorado Vendor Self Service (ColoradoVSS)**  
   https://vss.state.co.us/  
   The statewide vendor portal posts solicitations for most state agencies and many higher-education institutions. It does not include city and county solicitations and does not cover every university. Use it as one procurement discovery source, not as a complete contract registry.

## Initial records added

The first six Atlas records are intentionally limited to use cases with project-level descriptions in the OIT GenAI Projects document:

| Atlas record | Agency | Source-reported phase | Boundary preserved |
|---|---|---|---|
| CBMS — PANDA Policy Engine | HCPF | In production | Generalized policy research support; source says it does not make individual decisions |
| CBMS — Verification Document Automation | HCPF | In production | OCR/document extraction; source says a human reviews output; decision workflow remains to be checked |
| UI Virtual Agent and Claimant Chatbot | CDLE | Mixed production/pre-production features | Claimant information and self-service; source says responses do not inform individual decisions |
| Workers' Compensation Discovery Navigator | CDLE | Replacement in production; new features in development | Medical-record processing; source says it does not decide claim approvals |
| Recidiviz project | DOC | Pre-production / in planning | Staff support only; human review; not represented as a live Colorado deployment |
| HR Expert Systems Pilot | DPA | Approved, pre-production / pilot | Retrieval of public HR materials; source says it does not make decisions |

The Atlas uses **active**, **pilot**, or **planned** as normalized deployment states. These are transcriptions of the source's stated phase, not independent confirmation of current production operation. Vendor and model names are recorded only where the source states them. Procurement links, legal-source links, and oversight links remain empty until the underlying records are obtained and checked.

## Important exclusions and cautions

- The December 2025 tabular AI inventory contains many more rows than the six detailed project entries above. A production label does not by itself provide enough information to create a meaningful system record.
- The tabular inventory includes products whose AI functionality or specific agency use is not described in the document. Do not assume every listed software product is an AI system in the same technical or legal sense.
- OIT's GenAI Projects document explicitly excludes non-generative machine learning, agentic AI, and other non-generative methods. The Atlas must search for those systems separately.
- Agency statements that a system does not make decisions are preserved as source claims. They are not treated as an independent finding about actual workflow behavior.
- A system that supports a human decision may still influence a consequential outcome. The Atlas must investigate workflow placement, reliance, overrides, error rates, notice, appeal, and affected populations rather than assuming “human in the loop” settles the question.
- The source PDFs are dated December 2025. Reconfirm all statuses, vendors, model versions, and use cases against newer public records before describing them as current.

## Next evidence requests / collection tasks

1. Obtain the latest OIT AI inventory and the underlying agency-level ServiceHub inventory export, with appropriate redaction of security-sensitive details.
2. Collect OIT risk-assessment criteria, review outcomes, approval conditions, and monitoring requirements.
3. For each system, locate the contract, statement of work, amendments, data-processing terms, security addenda, and vendor/model change history.
4. Request or locate agency privacy assessments, data-flow diagrams, model evaluations, accuracy/error testing, accessibility testing, and incident/complaint logs.
5. Review the unemployment insurance, workers' compensation, Medicaid/CBMS, corrections, and HR workflows for any use of outputs in eligibility, enforcement, classification, or other consequential decisions.
6. Cross-reference State Auditor reports, legislative oversight materials, public rulemaking records, and public-records responses.
7. Expand coverage beyond GenAI to traditional machine learning, scoring, predictive analytics, automated eligibility, biometrics, and algorithmic workflow tools.

## Reproducibility and source discipline

Every record must identify the public source URL, the date checked, the source-reported deployment phase, and the limits of what the source establishes. Keep procurement evidence, operational evidence, and legal authority as separate links. Do not infer that an agency has no AI because a tool or contract is absent from a public inventory. Do not publish confidential security details, protected personal information, or non-public system prompts.
