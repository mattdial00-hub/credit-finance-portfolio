-- Q: Which loans failed a covenant at the April 2026 test, and by how much?
-- Skills: direction-aware cushion math, joining current grade
SELECT c.loan_id, b.name, b.industry, c.covenant,
       c.requirement, c.actual,
       ROUND(100.0 * CASE WHEN c.covenant LIKE 'Minimum%' THEN (c.actual - c.requirement) / c.requirement
                          ELSE (c.requirement - c.actual) / c.requirement END, 1) AS cushion_pct,
       s.risk_grade AS current_grade,
       ROUND(s.outstanding / 1e6, 2) AS outstanding_mm
FROM covenant_tests c
JOIN loans l     ON l.loan_id = c.loan_id
JOIN borrowers b ON b.borrower_id = l.borrower_id
JOIN quarterly_snapshots s ON s.loan_id = c.loan_id AND s.as_of_date = '2026-09-30'
WHERE c.test_date = '2026-04-30' AND c.result = 'Fail'
ORDER BY cushion_pct
LIMIT 25;
