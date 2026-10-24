-- Q: How much commitment matures in each of the next eight quarters?
-- Skills: date bucketing, pivot by facility type
SELECT substr(l.maturity_date, 1, 4) || '-Q' || ((CAST(substr(l.maturity_date, 6, 2) AS INTEGER) + 2) / 3) AS maturity_quarter,
       COUNT(*) AS loans,
       ROUND(SUM(l.commitment) / 1e6, 1) AS commitment_mm,
       ROUND(SUM(CASE WHEN l.facility_type = 'Revolving Line' THEN l.commitment ELSE 0 END) / 1e6, 1) AS revolver_mm,
       ROUND(SUM(CASE WHEN l.facility_type = 'CRE Term' THEN l.commitment ELSE 0 END) / 1e6, 1)       AS cre_term_mm,
       ROUND(SUM(CASE WHEN l.facility_type IN ('Term Loan', 'Equipment Loan') THEN l.commitment ELSE 0 END) / 1e6, 1) AS ci_term_mm,
       SUM(s.risk_grade >= 6) AS watch_or_worse
FROM loans l
JOIN quarterly_snapshots s ON s.loan_id = l.loan_id AND s.as_of_date = '2026-09-30'
WHERE l.maturity_date > '2026-09-30' AND l.maturity_date <= '2028-09-30' AND s.nonaccrual = 0
GROUP BY maturity_quarter
ORDER BY maturity_quarter;
