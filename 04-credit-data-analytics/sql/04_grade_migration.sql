-- Q: How did risk grades move over the last 12 months (count of loans)?
-- Skills: self-join across dates, pivot with conditional aggregation
WITH start AS (SELECT loan_id, risk_grade AS g0 FROM quarterly_snapshots WHERE as_of_date = '2025-09-30'),
     finish AS (SELECT loan_id, risk_grade AS g1 FROM quarterly_snapshots WHERE as_of_date = '2026-09-30')
SELECT s.g0 AS grade_sep_2025,
       SUM(f.g1 = 1) AS "1", SUM(f.g1 = 2) AS "2", SUM(f.g1 = 3) AS "3", SUM(f.g1 = 4) AS "4", SUM(f.g1 = 5) AS "5",
       SUM(f.g1 = 6) AS "6", SUM(f.g1 = 7) AS "7", SUM(f.g1 = 8) AS "8", SUM(f.g1 = 9) AS "9",
       SUM(f.g1 IS NULL) AS exited,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(f.g1 > s.g0) / COUNT(*), 1) AS downgrade_pct,
       ROUND(100.0 * SUM(f.g1 < s.g0) / COUNT(*), 1) AS upgrade_pct
FROM start s
LEFT JOIN finish f ON f.loan_id = s.loan_id
GROUP BY s.g0
ORDER BY s.g0;
