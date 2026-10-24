-- Q: Do some origination years perform worse than others?
-- Skills: LEFT JOIN to an event table, rates by cohort
SELECT CAST(substr(l.origination_date, 1, 4) AS INTEGER) AS vintage,
       COUNT(*)                                          AS loans,
       ROUND(SUM(l.commitment) / 1e6, 1)                 AS commitment_mm,
       COUNT(d.loan_id)                                  AS defaulted_loans,
       ROUND(100.0 * COUNT(d.loan_id) / COUNT(*), 2)     AS default_rate_pct,
       ROUND(COALESCE(SUM(d.loss_amount), 0) / 1e6, 2)   AS realized_loss_mm,
       ROUND(100.0 * COALESCE(SUM(d.loss_amount), 0) / SUM(l.commitment), 2) AS loss_rate_pct
FROM loans l
LEFT JOIN defaults d ON d.loan_id = l.loan_id
GROUP BY vintage
ORDER BY vintage;
