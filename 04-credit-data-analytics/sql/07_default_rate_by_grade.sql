-- Q: Do the bank's risk grades rank-order default risk? (12-month observed default rate by starting grade)
-- Skills: annual cohorts, date arithmetic, event window join
WITH cohorts AS (
    SELECT s.loan_id, l.borrower_id, s.as_of_date AS cohort_date, s.risk_grade
    FROM quarterly_snapshots s
    JOIN loans l ON l.loan_id = s.loan_id
    WHERE s.as_of_date IN ('2023-09-30', '2024-09-30', '2025-09-30') AND s.nonaccrual = 0
), borrower_cohorts AS (           -- one row per borrower per cohort, worst grade
    SELECT borrower_id, cohort_date, MAX(risk_grade) AS grade FROM cohorts GROUP BY borrower_id, cohort_date
), outcome AS (
    SELECT bc.*,
           EXISTS (SELECT 1 FROM defaults d
                   WHERE d.borrower_id = bc.borrower_id
                     AND d.default_date >  bc.cohort_date
                     AND d.default_date <= date(bc.cohort_date, '+12 months')) AS defaulted
    FROM borrower_cohorts bc
    WHERE bc.cohort_date <= date('2026-09-30', '-12 months')   -- full 12-month window observed
)
SELECT grade,
       COUNT(*)                                 AS borrower_years,
       SUM(defaulted)                           AS defaults,
       ROUND(100.0 * SUM(defaulted) / COUNT(*), 2) AS observed_default_rate_pct
FROM outcome
GROUP BY grade
ORDER BY grade;
