-- Q: Which pass-rated borrowers had a sharp drop in DSCR in their latest statements?
-- Skills: LAG() on financials, filtering on derived change, joining current exposure
WITH f AS (
    SELECT borrower_id, fiscal_year, dscr,
           LAG(dscr) OVER (PARTITION BY borrower_id ORDER BY fiscal_year) AS prior_dscr
    FROM financials
), latest AS (
    SELECT * FROM f WHERE fiscal_year = 2025 AND prior_dscr IS NOT NULL
), exposure AS (
    SELECT l.borrower_id, SUM(s.outstanding) AS outstanding, MAX(s.risk_grade) AS grade
    FROM loans l JOIN quarterly_snapshots s ON s.loan_id = l.loan_id AND s.as_of_date = '2026-09-30'
    GROUP BY l.borrower_id
)
SELECT b.name, b.industry, la.prior_dscr AS dscr_fy2024, la.dscr AS dscr_fy2025,
       ROUND(100.0 * (la.dscr / la.prior_dscr - 1), 1) AS dscr_change_pct,
       e.grade AS current_grade,
       ROUND(e.outstanding / 1e6, 2) AS outstanding_mm
FROM latest la
JOIN borrowers b ON b.borrower_id = la.borrower_id
JOIN exposure e  ON e.borrower_id = la.borrower_id
WHERE la.dscr / la.prior_dscr - 1 <= -0.20
  AND e.grade <= 5
ORDER BY dscr_change_pct
LIMIT 25;
