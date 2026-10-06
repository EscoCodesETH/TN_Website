# Product content evidence

Inspected 6 October 2026. UP³ product evidence is pinned to `EscoCodesETH/UP3` commit `69e042210be7f16a62c5ab3fbcb24690fc176f79`. This was a bounded read of product code and assertions for the website; no UP³ implementation was dispatched and no product tests were run.

## Verified claim basis

| Website claim | Evidence inspected |
| --- | --- |
| UP³ covers pay, personnel, reconciliation and travel; STARS is the travel product name | Product `README.md`, current implemented-code and claim-scope descriptions |
| Deterministic eligibility evaluation with unresolved facts, attestations and citations | `engine/src/modules/evaluation/determinations.ts`; `web/src/shared/ui/components.tsx` verdict metadata and source-excerpt UI |
| Recorded amounts can carry rate/source metadata; placeholder and uncorroborated amounts remain marked | `web/src/shared/ui/components.tsx`; `web/src/features/travel/components/DraftBreakdown.tsx` |
| Member record correction requests require office review; a request alone does not change a fact | `engine/test/record-review-routes.test.ts`, lines 78–100; personnel work-board source |
| Reconciliation produces candidate findings; human disposition is separate | `engine/src/modules/reconciliation/resolution.service.ts`, lines 614–624 |
| Member travel shows actions, authorizations, vouchers, documents and history | `web/src/features/travel/MyTravel.tsx`, current page contract and imports |
| Issued orders, authorization review and later voucher filing are distinct | `web/src/features/travel/MyTravel.tsx`, lines 1–18; travel source-basis contracts |
| Travel allowance explanations distinguish trip totals, rates, supplied inputs and waiting items | `web/src/features/travel/components/DraftBreakdown.tsx`, lines 49–134 |
| An allowance determination and voucher comparison are not payment | `DraftBreakdown.tsx` explicit payment boundary; `scripts/run-member-demo.mjs` demo boundary descriptions |
| Illustrative housing citations are real retained references | `spec/data/shared/entitlements/bah.json`, authority entries for 37 U.S.C. §403 and FMR-7A Chapter 26, lines 22857–22860 |

The synthetic housing example illustrates an unresolved-fact path. It is not a freshly calculated engine result, and its depiction does not assert entitlement eligibility or a payable amount. The STARS examples likewise illustrate workflow states without calculating allowances.

## Visual and demo provenance

The user confirmed that screenshots are not available. The current product tree contains no committed raster or vector screenshots. Every constructed visual is labeled **Workflow illustration · Synthetic data**; accessible descriptions identify its synthetic nature. These visuals are not captures of the live product UI. Genuine screenshots remain a future asset replacement when verified captures are supplied or their capture is separately authorized.

No public demo URL was supplied or verified. A local-only product launcher is not a visitor-facing demo link. Demo buttons therefore use the requested mailto fallback.

## Claim boundaries

The product README describes local synthetic development, without production deployment, external-system integration, authority to pay/post or an accredited security posture. The site presents the products as in development and invites a demonstration. It omits operational pilots, government relationships, partner logos, AI and blockchain claims. No future integration or planned deployment is described as implemented.

UP³ is described by its supplied function: Air Force pay, personnel and travel. Product documents use inconsistent long-form expansions of the brand, so this site does not select one. STARS is treated as the named travel service; no unverified acronym expansion is invented. LES, BAH, PCS, TDY and JTR are explained when introduced.
