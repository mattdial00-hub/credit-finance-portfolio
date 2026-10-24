-- Q: How has delinquency trended each quarter?
-- Skills: CASE bucketing, conditional aggregation
SELECT as_of_date,
       ROUND(SUM(outstanding) / 1e6, 1) AS outstanding_mm,
       ROUND(100.0 * SUM(CASE WHEN days_past_due = 0 THEN outstanding END) / SUM(outstanding), 2)                       AS current_pct,
       ROUND(100.0 * SUM(CASE WHEN days_past_due BETWEEN 1 AND 29 THEN outstanding ELSE 0 END) / SUM(outstanding), 2)  AS dpd_1_29_pct,
       ROUND(100.0 * SUM(CASE WHEN days_past_due BETWEEN 30 AND 89 THEN outstanding ELSE 0 END) / SUM(outstanding), 2) AS dpd_30_89_pct,
       ROUND(100.0 * SUM(CASE WHEN days_past_due >= 90 THEN outstanding ELSE 0 END) / SUM(outstanding), 2)             AS dpd_90_plus_pct,
       ROUND(100.0 * SUM(CASE WHEN nonaccrual = 1 THEN outstanding ELSE 0 END) / SUM(outstanding), 2)                  AS nonaccrual_pct,
       ROUND(100.0 * SUM(CASE WHEN risk_grade >= 7 THEN outstanding ELSE 0 END) / SUM(outstanding), 2)                 AS criticized_pct
FROM quarterly_snapshots
WHERE outstanding > 0
GROUP BY as_of_date
ORDER BY as_of_date;
