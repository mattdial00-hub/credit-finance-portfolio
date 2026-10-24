# SQL Query Results

Output of every query in [`sql/`](../sql/) run against `data/prairie_lantern_loans.db` (as of September 30, 2026). All data is fictional.

## 01_portfolio_summary.sql

**What does the commercial book look like today, by sector and industry?**

| sector | industry | loans | commitment_mm | outstanding_mm | pct_of_book | wtd_avg_grade | criticized_pct |
|---|---|---|---|---|---|---|---|
| CRE | CRE - Multifamily | 282 | 702.0 | 552.5 | 23.0 | 3.8 | 6.4 |
| CRE | CRE - Industrial | 191 | 456.8 | 370.5 | 15.5 | 3.06 | 0.0 |
| CRE | CRE - Office | 134 | 321.8 | 257.3 | 10.7 | 5.91 | 36.3 |
| CRE | CRE - Retail | 121 | 279.7 | 224.2 | 9.4 | 4.39 | 14.1 |
| CRE | CRE - Self Storage | 109 | 248.8 | 198.0 | 8.3 | 3.4 | 0.7 |
| CRE | CRE - Senior Housing | 75 | 172.9 | 138.8 | 5.8 | 4.86 | 19.8 |
| CRE | CRE - Hospitality | 60 | 116.6 | 93.0 | 3.9 | 5.03 | 21.3 |
| C&I | Manufacturing | 202 | 181.4 | 86.3 | 3.6 | 2.87 | 0.9 |
| C&I | Healthcare | 174 | 152.5 | 72.7 | 3.0 | 2.61 | 0.4 |
| C&I | Construction | 169 | 135.9 | 70.3 | 2.9 | 4.2 | 17.1 |
| C&I | Professional Services | 131 | 127.6 | 66.7 | 2.8 | 2.93 | 1.6 |
| C&I | Wholesale Distribution | 124 | 111.7 | 54.8 | 2.3 | 3.37 | 4.5 |
| C&I | Transportation | 136 | 110.8 | 51.5 | 2.1 | 4.03 | 6.7 |
| C&I | Energy Services | 106 | 83.6 | 43.6 | 1.8 | 3.88 | 4.9 |
| C&I | Restaurants | 80 | 74.6 | 42.3 | 1.8 | 4.33 | 10.6 |
| C&I | Retail Trade | 97 | 81.8 | 41.8 | 1.7 | 3.95 | 1.8 |
| C&I | Agriculture | 75 | 63.9 | 32.7 | 1.4 | 3.73 | 10.5 |

*17 rows*

## 02_top_relationships.sql

**Who are the 20 largest relationships, and how concentrated is the book?**

| rnk | name | industry | commitment_mm | outstanding_mm | worst_grade | pct_of_total | cumulative_pct |
|---|---|---|---|---|---|---|---|
| 1 | Eastfield Business Park, Ltd. | CRE - Industrial | 15.23 | 14.44 | 3 | 0.44 | 0.4 |
| 2 | Granite Ridge Office Center, LLC | CRE - Office | 13.65 | 9.45 | 9 | 0.4 | 0.8 |
| 3 | Granite Ridge Business Park, Inc. | CRE - Industrial | 12.69 | 10.56 | 4 | 0.37 | 1.2 |
| 4 | Falcon Point Residences, LP | CRE - Multifamily | 12.68 | 10.09 | 7 | 0.37 | 1.6 |
| 5 | Stonegate Storage, LP | CRE - Self Storage | 12.51 | 10.48 | 4 | 0.36 | 1.9 |
| 6 | Copper Creek Industrial Park, LP | CRE - Industrial | 12.37 | 7.35 | 2 | 0.36 | 2.3 |
| 7 | Caddo Business Park, Ltd. | CRE - Industrial | 12.11 | 9.92 | 5 | 0.35 | 2.6 |
| 8 | Mesquite Business Park, Ltd. | CRE - Industrial | 10.91 | 9.67 | 6 | 0.32 | 3.0 |
| 9 | Frio Apartments, LP | CRE - Multifamily | 10.64 | 10.23 | 5 | 0.31 | 3.3 |
| 10 | Highland Tower, LP | CRE - Office | 10.12 | 9.06 | 6 | 0.29 | 3.6 |
| 11 | Highland Village, Inc. | CRE - Multifamily | 10.11 | 7.82 | 8 | 0.29 | 3.9 |
| 12 | Sabine Senior Living, Inc. | CRE - Senior Housing | 9.9 | 7.56 | 3 | 0.29 | 4.1 |
| 13 | Cedar Bayou Storage, Inc. | CRE - Self Storage | 9.87 | 8.41 | 4 | 0.29 | 4.4 |
| 14 | Sabine Village, LLC | CRE - Multifamily | 9.84 | 5.29 | 2 | 0.29 | 4.7 |
| 15 | Lone Star Tower, Inc. | CRE - Office | 9.65 | 7.01 | 7 | 0.28 | 5.0 |
| 16 | Copper Creek Residences, LP | CRE - Multifamily | 9.49 | 8.09 | 4 | 0.28 | 5.3 |
| 17 | Cypress Shopping Center, Inc. | CRE - Retail | 9.47 | 8.66 | 4 | 0.27 | 5.6 |
| 18 | Twin Oaks Office Center, LLC | CRE - Office | 9.35 | 8.73 | 8 | 0.27 | 5.8 |
| 19 | Trinity Village, Inc. | CRE - Multifamily | 9.35 | 7.24 | 6 | 0.27 | 6.1 |
| 20 | Cedar Bayou Self Storage, LLC | CRE - Self Storage | 9.21 | 8.24 | 3 | 0.27 | 6.4 |

*20 rows*

## 03_delinquency_trend.sql

**How has delinquency trended each quarter?**

| as_of_date | outstanding_mm | current_pct | dpd_1_29_pct | dpd_30_89_pct | dpd_90_plus_pct | nonaccrual_pct | criticized_pct |
|---|---|---|---|---|---|---|---|
| 2023-03-31 | 1,693.10 | 96.95 | 2.18 | 0.8 | 0.06 | 0.06 | 2.95 |
| 2023-06-30 | 1,798.70 | 96.72 | 2.44 | 0.27 | 0.57 | 0.57 | 2.2 |
| 2023-09-30 | 1,888.00 | 97.22 | 1.8 | 0.39 | 0.59 | 0.59 | 2.39 |
| 2023-12-31 | 1,982.10 | 96.68 | 2.7 | 0.26 | 0.36 | 0.36 | 2.3 |
| 2024-03-31 | 2,062.30 | 95.97 | 2.29 | 1.27 | 0.47 | 0.47 | 3.15 |
| 2024-06-30 | 2,162.20 | 95.32 | 1.98 | 1.37 | 1.32 | 1.32 | 8.39 |
| 2024-09-30 | 2,250.20 | 93.93 | 2.37 | 1.27 | 2.42 | 2.42 | 8.39 |
| 2024-12-31 | 2,292.70 | 94.15 | 3.02 | 0.78 | 2.04 | 2.04 | 7.33 |
| 2025-03-31 | 2,319.10 | 95.42 | 2.75 | 0.9 | 0.94 | 0.94 | 6.7 |
| 2025-06-30 | 2,369.70 | 94.86 | 3.75 | 0.47 | 0.93 | 0.93 | 11.07 |
| 2025-09-30 | 2,456.00 | 94.64 | 3.33 | 1.2 | 0.84 | 0.84 | 10.81 |
| 2025-12-31 | 2,559.10 | 93.99 | 3.79 | 0.88 | 1.34 | 1.34 | 10.39 |
| 2026-03-31 | 2,511.30 | 94.52 | 2.49 | 1.43 | 1.55 | 1.55 | 11.36 |
| 2026-06-30 | 2,448.90 | 92.7 | 3.92 | 1.51 | 1.87 | 1.87 | 10.64 |
| 2026-09-30 | 2,397.10 | 95.05 | 2.13 | 0.2 | 2.63 | 2.63 | 10.01 |

*15 rows*

## 04_grade_migration.sql

**How did risk grades move over the last 12 months (count of loans)?**

| grade_sep_2025 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | exited | total | downgrade_pct | upgrade_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 63 | 51 | 34 | 13 | 4 | 0 | 0 | 2 | 0 | 0 | 167 | 62.3 | 0.0 |
| 2 | 64 | 124 | 115 | 57 | 10 | 1 | 1 | 4 | 1 | 0 | 377 | 50.1 | 17.0 |
| 3 | 39 | 108 | 97 | 115 | 49 | 16 | 7 | 2 | 1 | 0 | 434 | 43.8 | 33.9 |
| 4 | 10 | 82 | 113 | 134 | 80 | 39 | 12 | 10 | 1 | 0 | 481 | 29.5 | 42.6 |
| 5 | 5 | 24 | 79 | 88 | 84 | 55 | 21 | 6 | 4 | 0 | 366 | 23.5 | 53.6 |
| 6 | 2 | 6 | 24 | 43 | 40 | 52 | 41 | 11 | 1 | 0 | 220 | 24.1 | 52.3 |
| 7 | 0 | 0 | 5 | 11 | 22 | 37 | 50 | 3 | 2 | 22 | 152 | 3.3 | 49.3 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 24 | 27 | 7.4 | 0.0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 10 | 0.0 | 20.0 |

*9 rows*

## 05_roll_rates.sql

**Quarter to quarter, how often do loans roll into worse delinquency buckets?**

| from_bucket | loan_quarters | to_current_pct | to_1_29_pct | to_30_89_pct | to_90_plus_pct |
|---|---|---|---|---|---|
| 1: Current | 25843 | 96.49 | 2.58 | 0.77 | 0.16 |
| 2: 1-29 | 689 | 93.03 | 4.06 | 2.47 | 0.44 |
| 3: 30-89 | 231 | 38.96 | 3.9 | 1.73 | 55.41 |
| 4: 90+ / nonaccrual | 288 | 0.0 | 0.0 | 0.0 | 100.0 |

*4 rows*

## 06_vintage_analysis.sql

**Do some origination years perform worse than others?**

| vintage | loans | commitment_mm | defaulted_loans | default_rate_pct | realized_loss_mm | loss_rate_pct |
|---|---|---|---|---|---|---|
| 2015 | 121 | 199.3 | 12 | 9.92 | 3.26 | 1.64 |
| 2016 | 103 | 152.7 | 11 | 10.68 | 1.11 | 0.73 |
| 2017 | 115 | 194.5 | 14 | 12.17 | 2.23 | 1.15 |
| 2018 | 162 | 228.1 | 8 | 4.94 | 0.91 | 0.4 |
| 2019 | 190 | 282.3 | 15 | 7.89 | 4.82 | 1.71 |
| 2020 | 190 | 269.7 | 15 | 7.89 | 3.02 | 1.12 |
| 2021 | 216 | 328.0 | 17 | 7.87 | 5.09 | 1.55 |
| 2022 | 272 | 413.4 | 24 | 8.82 | 6.03 | 1.46 |
| 2023 | 319 | 547.9 | 28 | 8.78 | 15.47 | 2.82 |
| 2024 | 347 | 519.9 | 21 | 6.05 | 7.55 | 1.45 |
| 2025 | 364 | 523.0 | 10 | 2.75 | 1.61 | 0.31 |

*11 rows*

## 07_default_rate_by_grade.sql

**Do the bank's risk grades rank-order default risk? (12-month observed default rate by starting grade)**

| grade | borrower_years | defaults | observed_default_rate_pct |
|---|---|---|---|
| 1 | 191 | 1 | 0.52 |
| 2 | 632 | 4 | 0.63 |
| 3 | 858 | 3 | 0.35 |
| 4 | 924 | 17 | 1.84 |
| 5 | 718 | 16 | 2.23 |
| 6 | 393 | 17 | 4.33 |
| 7 | 226 | 28 | 12.39 |
| 8 | 5 | 4 | 80.0 |
| 9 | 2 | 2 | 100.0 |

*9 rows*

## 08_lgd_by_collateral.sql

**How much do we lose when loans default, by collateral type? (resolved defaults only)**

| collateral_type | resolved_defaults | ead_mm | loss_mm | ead_weighted_lgd_pct | simple_avg_lgd_pct | avg_days_to_resolve |
|---|---|---|---|---|---|---|
| Business assets (blanket) | 16 | 6.21 | 3.14 | 50.5 | 46.7 | 228.0 |
| A/R and inventory | 39 | 20.35 | 8.76 | 43.1 | 41.3 | 228.0 |
| Equipment (PMSI) | 11 | 2.76 | 0.91 | 32.9 | 39.7 | 234.0 |
| Real estate (1st lien) | 67 | 145.79 | 38.29 | 26.3 | 26.1 | 235.0 |

*4 rows*

## 09_covenant_exceptions.sql

**Which loans failed a covenant at the April 2026 test, and by how much?**

| loan_id | name | industry | covenant | requirement | actual | cushion_pct | current_grade | outstanding_mm |
|---|---|---|---|---|---|---|---|---|
| L5463 | Lone Star Electric, LP | Construction | Maximum Funded Debt / EBITDA | 3.0 | 7.09 | -136.3 | 7 | 0.08 |
| L5464 | Lone Star Electric, LP | Construction | Maximum Funded Debt / EBITDA | 3.5 | 7.09 | -102.6 | 7 | 1.18 |
| L6011 | Sandstone Trucking, LLC | Transportation | Maximum Funded Debt / EBITDA | 3.0 | 6.01 | -100.3 | 7 | 0.39 |
| L5384 | Clearfork Medical Group, Inc. | Healthcare | Maximum Funded Debt / EBITDA | 3.5 | 6.46 | -84.6 | 8 | 0.0 |
| L5385 | Clearfork Medical Group, Inc. | Healthcare | Maximum Funded Debt / EBITDA | 3.5 | 6.46 | -84.6 | 9 | 0.0 |
| L7369 | Stonegate Trucking, LP | Transportation | Maximum Funded Debt / EBITDA | 3.0 | 5.38 | -79.3 | 7 | 0.02 |
| L7371 | Stonegate Trucking, LP | Transportation | Maximum Funded Debt / EBITDA | 3.0 | 5.38 | -79.3 | 7 | 0.28 |
| L5121 | Bluebonnet Outfitters, Ltd. | Retail Trade | Maximum Funded Debt / EBITDA | 3.0 | 5.3 | -76.7 | 7 | 0.25 |
| L7296 | Riverbend Restaurant Group, LP | Restaurants | Maximum Funded Debt / EBITDA | 3.0 | 5.18 | -72.7 | 7 | 0.02 |
| L6012 | Sandstone Trucking, LLC | Transportation | Maximum Funded Debt / EBITDA | 3.5 | 6.01 | -71.7 | 6 | 0.42 |
| L6042 | Bayside Physical Therapy, LP | Healthcare | Maximum Funded Debt / EBITDA | 3.0 | 5.06 | -68.7 | 4 | 0.22 |
| L6903 | Frio Construction, LP | Construction | Maximum Funded Debt / EBITDA | 3.0 | 4.95 | -65.0 | 7 | 0.53 |
| L6627 | Harborview Oilfield Services, LLC | Energy Services | Maximum Funded Debt / EBITDA | 3.0 | 4.9 | -63.3 | 9 | 0.0 |
| L7376 | Cypress Office Center, LP | CRE - Office | Maximum LTV | 0.75 | 1.199 | -59.9 | 7 | 1.63 |
| L7377 | Cypress Office Center, LP | CRE - Office | Maximum LTV | 0.75 | 1.199 | -59.9 | 7 | 1.12 |
| L7056 | Granite Ridge Office Center, LLC | CRE - Office | Maximum LTV | 0.75 | 1.184 | -57.9 | 8 | 1.07 |
| L7057 | Granite Ridge Office Center, LLC | CRE - Office | Maximum LTV | 0.75 | 1.184 | -57.9 | 9 | 1.61 |
| L7058 | Granite Ridge Office Center, LLC | CRE - Office | Maximum LTV | 0.75 | 1.184 | -57.9 | 8 | 6.76 |
| L6572 | Harborview Electric, LP | Construction | Maximum Funded Debt / EBITDA | 3.0 | 4.65 | -55.0 | 7 | 0.03 |
| L7370 | Stonegate Trucking, LP | Transportation | Maximum Funded Debt / EBITDA | 3.5 | 5.38 | -53.7 | 7 | 0.26 |
| L7222 | Magnolia Supply, Inc. | Wholesale Distribution | Maximum Funded Debt / EBITDA | 3.0 | 4.53 | -51.0 | 4 | 0.06 |
| L5393 | Cedar Bayou Dental, LP | Healthcare | Maximum Funded Debt / EBITDA | 3.0 | 4.47 | -49.0 | 5 | 0.39 |
| L7143 | Twin Oaks Medical Group, LP | Healthcare | Maximum Funded Debt / EBITDA | 3.0 | 4.43 | -47.7 | 6 | 0.06 |
| L5889 | Guadalupe Trucking, Inc. | Transportation | Maximum Funded Debt / EBITDA | 3.0 | 4.42 | -47.3 | 6 | 0.07 |
| L5877 | Stonegate Industries, Inc. | Manufacturing | Maximum Funded Debt / EBITDA | 3.0 | 4.39 | -46.3 | 2 | 0.07 |

*25 rows*

## 10_maturity_ladder.sql

**How much commitment matures in each of the next eight quarters?**

| maturity_quarter | loans | commitment_mm | revolver_mm | cre_term_mm | ci_term_mm | watch_or_worse |
|---|---|---|---|---|---|---|
| 2026-Q4 | 104 | 253.4 | 0.0 | 253.4 | 0.0 | 20 |
| 2027-Q1 | 238 | 247.4 | 174.7 | 48.5 | 24.1 | 32 |
| 2027-Q2 | 243 | 260.1 | 149.7 | 82.8 | 27.6 | 34 |
| 2027-Q3 | 214 | 235.6 | 139.9 | 73.1 | 22.5 | 23 |
| 2027-Q4 | 246 | 233.7 | 147.2 | 67.7 | 18.8 | 33 |
| 2028-Q1 | 49 | 83.4 | 0.0 | 54.4 | 29.0 | 7 |
| 2028-Q2 | 59 | 105.8 | 0.0 | 78.1 | 27.6 | 15 |
| 2028-Q3 | 54 | 95.9 | 0.0 | 68.6 | 27.3 | 12 |

*8 rows*

## 11_early_warning.sql

**Which pass-rated borrowers had a sharp drop in DSCR in their latest statements?**

| name | industry | dscr_fy2024 | dscr_fy2025 | dscr_change_pct | current_grade | outstanding_mm |
|---|---|---|---|---|---|---|
| Nueces Oilfield Services, Inc. | Energy Services | 1.98 | 1.3 | -34.3 | 5 | 1.31 |
| Granite Ridge Office Plaza, LP | CRE - Office | 1.53 | 1.06 | -30.7 | 5 | 2.06 |
| Northline Engineering, Inc. | Professional Services | 2.25 | 1.58 | -29.8 | 5 | 0.76 |
| Mesquite Fabrication, LP | Manufacturing | 1.87 | 1.32 | -29.4 | 5 | 0.03 |
| Sandstone Business Park, Ltd. | CRE - Industrial | 1.43 | 1.03 | -28.0 | 5 | 2.02 |
| Highland Apartments, LLC | CRE - Multifamily | 2.06 | 1.49 | -27.7 | 4 | 0.48 |
| Trinity Self Storage, LLC | CRE - Self Storage | 2.4 | 1.75 | -27.1 | 4 | 0.9 |
| Frio Apartments, LP | CRE - Multifamily | 1.96 | 1.43 | -27.0 | 5 | 10.23 |
| Copper Creek Oilfield Services, LLC | Energy Services | 1.84 | 1.35 | -26.6 | 5 | 0.61 |
| Live Oak Construction, Ltd. | Construction | 4.31 | 3.17 | -26.5 | 2 | 0.07 |
| Sabine Construction, Ltd. | Construction | 1.62 | 1.19 | -26.5 | 5 | 0.51 |
| Gulfline Office Plaza, LLC | CRE - Office | 1.84 | 1.37 | -25.5 | 5 | 1.22 |
| Sandstone Supply, Ltd. | Wholesale Distribution | 1.67 | 1.27 | -24.0 | 4 | 0.05 |
| Granite Ridge Business Park, Inc. | CRE - Industrial | 2.72 | 2.07 | -23.9 | 4 | 10.56 |
| Red River Distribution Center, LP | CRE - Industrial | 1.93 | 1.47 | -23.8 | 4 | 3.34 |
| Highland Machine Works, Inc. | Manufacturing | 1.74 | 1.33 | -23.6 | 5 | 1.14 |
| Falcon Point Pipeline Services, LLC | Energy Services | 2.16 | 1.65 | -23.6 | 5 | 0.05 |
| Lone Star Industrial Park, Inc. | CRE - Industrial | 2.1 | 1.61 | -23.3 | 3 | 3.96 |
| Red River Residences, Ltd. | CRE - Multifamily | 1.17 | 0.9 | -23.1 | 5 | 5.77 |
| Guadalupe Distribution Center, Ltd. | CRE - Industrial | 2.38 | 1.83 | -23.1 | 4 | 2.9 |
| Stonegate Oilfield Services, LLC | Energy Services | 2.49 | 1.92 | -22.9 | 3 | 0.43 |
| Highland Residences, Inc. | CRE - Multifamily | 1.59 | 1.23 | -22.6 | 5 | 5.26 |
| Harborview Medical Group, Inc. | Healthcare | 3.12 | 2.43 | -22.1 | 2 | 0.76 |
| Silverleaf Electric, LLC | Construction | 2.11 | 1.65 | -21.8 | 4 | 0.4 |
| Twin Oaks Dental, Ltd. | Healthcare | 2.26 | 1.77 | -21.7 | 4 | 0.87 |

*25 rows*

## 12_net_charge_offs.sql

**What are annual net charge-offs as a share of average loans outstanding?**

| year | charge_offs_mm | avg_outstanding_mm | nco_rate_pct |
|---|---|---|---|
| 2023 | 4.06 | 1,846.90 | 0.22 |
| 2024 | 17.19 | 2,196.10 | 0.783 |
| 2025 | 18.37 | 2,429.80 | 0.756 |
| 2026 | 16.46 | 2,452.70 | 0.671 |

*4 rows*

## 13_expected_loss.sql

**What is the 12-month expected loss on the current book, using the PD model?**

| industry | ead_mm | wtd_pd_pct | el_rate_pct | expected_loss_k |
|---|---|---|---|---|
| TOTAL | 2,444.40 | 3.17 | 0.903 | 22,066.00 |
| CRE - Office | 229.8 | 16.89 | 4.436 | 10,196.00 |
| CRE - Hospitality | 93.0 | 8.26 | 2.169 | 2,017.00 |
| CRE - Senior Housing | 129.1 | 5.73 | 1.506 | 1,945.00 |
| CRE - Multifamily | 541.9 | 1.14 | 0.299 | 1,620.00 |
| Construction | 81.7 | 3.11 | 1.33 | 1,086.00 |
| CRE - Retail | 215.4 | 1.84 | 0.484 | 1,043.00 |
| Transportation | 64.1 | 3.33 | 1.428 | 916.0 |
| Restaurants | 47.4 | 3.64 | 1.515 | 717.0 |
| Energy Services | 52.6 | 2.65 | 1.177 | 620.0 |
| Retail Trade | 47.5 | 2.25 | 0.97 | 461.0 |
| CRE - Industrial | 370.5 | 0.46 | 0.12 | 445.0 |
| CRE - Self Storage | 198.0 | 0.78 | 0.204 | 405.0 |
| Manufacturing | 104.7 | 0.41 | 0.175 | 183.0 |
| Healthcare | 86.4 | 0.29 | 0.122 | 105.0 |
| Agriculture | 39.3 | 0.64 | 0.266 | 105.0 |
| Wholesale Distribution | 63.9 | 0.38 | 0.158 | 101.0 |
| Professional Services | 78.9 | 0.3 | 0.128 | 101.0 |

*18 rows*
