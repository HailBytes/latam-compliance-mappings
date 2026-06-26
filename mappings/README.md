# Product → Framework Mappings — Coverage Index

This directory contains mappings between HailBytes products and Latin American
compliance frameworks. Each mapping document links specific product features to
the framework articles a documented control program helps satisfy, and notes the
evidence each control generates.

> **What "not yet mapped" means:** A blank cell below indicates that a published
> mapping document does **not yet exist** for that product/framework pair. It is
> **not** a statement that the product lacks relevant capability, nor a commitment
> that a control is in or out of scope. Product capability is described in the
> respective product documentation; this index tracks **documentation coverage only.**

## Coverage Matrix

| Framework | Region | HailBytes SAT | HailBytes ASM |
|---|---|---|---|
| **LGPD** | 🇧🇷 Brazil | ✅ [SAT → LGPD](./hailbytes-sat-to-lgpd.md) | ⬜ Not yet mapped |
| **BACEN Res. 4.893** | 🇧🇷 Brazil (Financial) | ⬜ Not yet mapped | ✅ [ASM → BACEN 4.893](./hailbytes-asm-to-bacen-4893.md) |
| **BACEN Res. 4.658** | 🇧🇷 Brazil (Financial) | ⬜ Not yet mapped | ⬜ Not yet mapped (superseded by 4.893) |
| **Marco Civil da Internet** | 🇧🇷 Brazil | ⬜ Not yet mapped | ⬜ Not yet mapped |
| **LFPDPPP** | 🇲🇽 Mexico | ✅ [SAT → LFPDPPP](./hailbytes-sat-to-lfpdppp.md) | ⬜ Not yet mapped |
| **Ley 25.326** | 🇦🇷 Argentina | ⬜ Not yet mapped | ⬜ Not yet mapped |
| **ISO 27001:2022** | 🌎 Regional | ⬜ Not yet mapped | ⬜ Not yet mapped |
| **NIST CSF 2.0** | 🌎 Regional | ⬜ Not yet mapped | ⬜ Not yet mapped |

**Legend:** ✅ published mapping · ⬜ not yet mapped (documentation status, not capability)

## Published Mappings

| Mapping | Product | Framework | Last Updated |
|---|---|---|---|
| [hailbytes-sat-to-lgpd.md](./hailbytes-sat-to-lgpd.md) | SAT | LGPD (Brazil) | 2026-05-18 |
| [hailbytes-asm-to-bacen-4893.md](./hailbytes-asm-to-bacen-4893.md) | ASM | BACEN 4.893 (Brazil) | 2026-05-18 |
| [hailbytes-sat-to-lfpdppp.md](./hailbytes-sat-to-lfpdppp.md) | SAT | LFPDPPP (Mexico) | 2026-05-18 |

## How to Read a Mapping

Every mapping document follows the same structure:

1. **Header** — product, framework, last-updated date, and the product version mapped.
2. **About / deployment model** — how the product is deployed (BYOC) and what that
   means for the control boundary.
3. **Shared-responsibility callout** — a pointer to
   [`docs/byoc-shared-responsibility-matrix.md`](../docs/byoc-shared-responsibility-matrix.md),
   which is the authoritative A/B/C breakdown of HailBytes-shipped vs.
   customer-configured vs. customer-organizational responsibilities.
4. **Compliance mapping table** — framework article → requirement → product feature → evidence generated.

Mapping claims are deliberately scoped to shipped product capability. Where a
control depends on customer configuration (region, key custody, retention windows)
or on customer organizational process, the mapping says so and defers to the
shared-responsibility matrix.

---

> All mappings are provided for informational purposes and reference public
> regulatory text. Consult qualified legal counsel before relying on them for a
> specific compliance program.
