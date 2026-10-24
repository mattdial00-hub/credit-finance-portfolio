-- Q: How much do we lose when loans default, by collateral type? (resolved defaults only)
-- Skills: exposure-weighted averages vs simple averages
SELECT l.collateral_type,
       COUNT(*)                                            AS resolved_defaults,
       ROUND(SUM(d.exposure_at_default) / 1e6, 2)          AS ead_mm,
       ROUND(SUM(d.loss_amount) / 1e6, 2)                  AS loss_mm,
       ROUND(100.0 * SUM(d.loss_amount) / SUM(d.exposure_at_default), 1) AS ead_weighted_lgd_pct,
       ROUND(100.0 * AVG(d.lgd), 1)                        AS simple_avg_lgd_pct,
       ROUND(AVG(julianday(d.resolution_date) - julianday(d.default_date)), 0) AS avg_days_to_resolve
FROM defaults d
JOIN loans l ON l.loan_id = d.loan_id
WHERE d.status = 'Resolved'
GROUP BY l.collateral_type
ORDER BY ead_weighted_lgd_pct DESC;
