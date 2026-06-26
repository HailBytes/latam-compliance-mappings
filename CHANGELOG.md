# Changelog

All notable changes to the HailBytes LatAm Compliance Mappings are documented here.

This repository is a compliance reference; entries focus on the **accuracy and
currency of regulatory citations and product-capability claims**. The format is
loosely based on [Keep a Changelog](https://keepachangelog.com/), and dates use
ISO 8601 (YYYY-MM-DD).

## [Unreleased]

### Changed
- **Mexico LFPDPPP updated for the 2025 reform.** `frameworks/mexico/lfpdppp.md`
  now reflects that the 2010 statute was abrogated and replaced by a new LFPDPPP
  effective 2025-03-21, and that INAI was dissolved with its data-protection
  mandate transferred to the Secretaría Anticorrupción y Buen Gobierno (SABG).
  README coverage row and the SAT → LFPDPPP mapping note updated accordingly.
- **ANPD breach-notification citation fully unified to Res. CD/ANPD No. 15/2024.**
  Remaining `15/2023` references in the incident-response runbook, the data
  processing agreement template, and the NIST CSF (Portuguese) notes were
  corrected, completing the unification claimed in the 2026-05-18 audit (G14)
  and matching the deprecation guidance in `docs/glossary.md`.

### Added
- **Mappings coverage index** (`mappings/README.md`) — a product × framework
  matrix showing which mappings are published vs. not yet mapped, with an
  explicit note that "not yet mapped" reflects documentation status, not product
  capability.
- **README discoverability** — the shared-responsibility matrix and glossary
  (added 2026-05-18) are now linked from the README Quick Links and BYOC section.
- This `CHANGELOG.md`.

## [2026-05-18] — Cross-repo alignment audit (PR #2)

### Added
- `docs/byoc-shared-responsibility-matrix.md` — A/B/C bucket breakdown of which
  compliance claims are guaranteed by HailBytes code, depend on customer
  Terraform/configuration, or are customer-organizational responsibilities.
- `docs/glossary.md` — canonical cross-repo terminology (RBAC, MFA, BYOC tiers,
  CMK, SBOM, completion certificates, LatAm regulator acronyms).
- `audit/cross-repo-alignment-2026-05-18.md` — audit trail mapping 14 findings to
  remediation.

### Changed
- Compliance mappings rewritten to reference the actual 20 built-in SAT training
  modules (M01–M20) and signed PDF completion certificates.
- Deployment tiers (Tier 1 Marketplace VM vs. Tier 2/3 Terraform) made explicit,
  clarifying customer-managed KMS/CMK key custody and region-selection
  responsibility; unsupported region-pinning claims removed.
- BACEN incident-notification citations corrected to Art. 12–13; ANPD citation
  unified to Res. CD/ANPD No. 15/2024 with "3 business days" wording.

## [2026-05-17] — Capability-claim accuracy audit (PR #1)

### Changed
- Corrected product-capability claims across mappings, frameworks, and docs to
  match shipped functionality: removed non-existent features (data-minimization
  modules, attestation workflow, tabletop exercises, supplier risk scores,
  "immutable" audit-log qualifier), and fixed regional/region claims (Argentina
  has no dedicated AWS/Azure region; SAT ships via Marketplace, not IaC).
- Corrected the LGPD vs. GDPR breach-notification deadline and the Enterprise
  SLA critical-response figure.
