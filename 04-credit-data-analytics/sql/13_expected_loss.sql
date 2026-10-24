-- Q: What is the 12-month expected loss on the current book, using the PD model?
-- EL = PD x LGD x EAD. PD from the model (pd_scores table, written by the notebook).
-- EAD = outstanding + 50% of the undrawn revolver commitment. LGD = realized loss history by collateral type.
WITH lgd AS (                  -- historical EAD-weighted LGD by collateral type (same logic as query 08)
    SELECT l.collateral_type, SUM(d.loss_amount) / SUM(d.exposure_at_default) AS lgd
    FROM defaults d JOIN loans l ON l.loan_id = d.loan_id
    WHERE d.status = 'Resolved'
    GROUP BY l.collateral_type
), book AS (
    SELECT l.loan_id, b.industry, b.sector, p.pd, g.lgd,
           s.outstanding + CASE WHEN l.facility_type = 'Revolving Line' THEN 0.5 * (l.commitment - s.outstanding) ELSE 0 END AS ead
    FROM quarterly_snapshots s
    JOIN loans l     ON l.loan_id = s.loan_id
    JOIN borrowers b ON b.borrower_id = l.borrower_id
    JOIN pd_scores p ON p.borrower_id = l.borrower_id
    JOIN lgd g       ON g.collateral_type = l.collateral_type
    WHERE s.as_of_date = '2026-09-30' AND s.nonaccrual = 0
)
SELECT industry,
       ROUND(SUM(ead) / 1e6, 1)                         AS ead_mm,
       ROUND(100.0 * SUM(pd * ead) / SUM(ead), 2)       AS wtd_pd_pct,
       ROUND(100.0 * SUM(pd * lgd * ead) / SUM(ead), 3) AS el_rate_pct,
       ROUND(SUM(pd * lgd * ead) / 1e3, 0)              AS expected_loss_k
FROM book
GROUP BY industry
UNION ALL
SELECT 'TOTAL', ROUND(SUM(ead) / 1e6, 1), ROUND(100.0 * SUM(pd * ead) / SUM(ead), 2),
       ROUND(100.0 * SUM(pd * lgd * ead) / SUM(ead), 3), ROUND(SUM(pd * lgd * ead) / 1e3, 0)
FROM book
ORDER BY expected_loss_k DESC;
