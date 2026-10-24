# 01 | Commercial Credit Package: Brazos Bend Fabrication, LLC

A complete underwriting package for a fictional Gulf Coast metal fabricator requesting a **$2.8MM equipment term loan** and a **revolving line increase to $1.5MM**. It follows the workflow a commercial credit analyst uses from spreading to recommendation.

> **Fictional work sample.** The borrower, guarantors, bank (Prairie Lantern Bank, N.A.), and all figures were created for demonstration. No real customer or employer data is used.

## Deal at a glance

| Metric | Result | Policy | |
|---|---|---|---|
| Historical pro forma DSCR | 1.31x | 1.25x min | ✅ |
| Projected Year 1 DSCR | 1.81x | 1.25x min | ✅ |
| Global DSCR | 1.40x | 1.20x min | ✅ |
| Pro forma funded debt / EBITDA | 2.35x | 3.0x max | ✅ |
| Collateral coverage | 1.13x | 1.00x min | ✅ |
| Breakeven revenue decline (1.00x) | 12.0% | | ⚠️ Key risk |
| Risk rating | 4, Satisfactory | 9-point scale | |
| **Recommendation** | **Approve with covenants** | | |

## Files

| File | What it is |
|---|---|
| [00_Deal_Scenario.md](00_Deal_Scenario.md) | The borrower, request, and background a credit analyst would receive |
| [Credit_Analysis_Model.xlsx](Credit_Analysis_Model.xlsx) | Live, formula-driven Excel model (10 tabs, 700+ formulas) |
| [Credit_Memo_Brazos_Bend.pdf](Credit_Memo_Brazos_Bend.pdf) | Six-page credit memorandum with recommendation (also in [.docx](Credit_Memo_Brazos_Bend.docx)) |
| [Industry_Risk_Brief.md](Industry_Risk_Brief.md) | Industry and market risk assessment for fabricated metal manufacturing |
| [SBA_7a_Underwriting_Checklist.md](SBA_7a_Underwriting_Checklist.md) | SBA 7(a) eligibility and underwriting checklist |

## Inside the model

| Tab | Skill demonstrated |
|---|---|
| **Inputs** | Deal structuring: advance rates, pricing, equity injection, policy limits |
| **Spread** | Three-year income statement and balance sheet spread with equity roll-forward and derived cash flow; every tie-out check is zero |
| **Ratios** | Profitability, liquidity, working capital cycle (DSO, DIO, DPO), leverage, DSCR, fixed charge coverage |
| **Global_CF** | Guarantor cash flow with taxes on K-1 income (not just distributions), personal debt, post-closing liquidity |
| **ProForma_DSCR** | Coverage of new debt on actual FY2025 cash flow, plus a projected Year 1 case with stated assumptions |
| **Stress_Test** | Revenue, margin, and rate shocks using a contribution margin approach; breakeven revenue decline |
| **Risk_Rating** | Weighted scorecard pulling live metrics into banded scores |
| **Collateral_BB** | Collateral coverage on total exposure and a borrowing base certificate tied to the balance sheet |
| **Amortization** | 84-month schedule feeding Year 1 interest into the projection |

**Color legend:** blue = input, black = formula, green = link to another tab, yellow = key output or policy test. Change any blue cell and the whole model recalculates.

## Analyst judgment calls worth noting

- **Distributions are deducted** in DSCR because the owners need them to pay taxes on pass-through income.
- **Personal taxes are applied to K-1 taxable income**, not cash distributed, which is the conservative treatment in global cash flow.
- **Management's 2.0% margin benefit is haircut to 1.5%**, and approval does not depend on it: historical pro forma DSCR passes with zero credit for the new equipment.
- **Stress testing exposed thin coverage** in a downturn, so the structure adds a distribution restriction if DSCR drops below 1.35x.
