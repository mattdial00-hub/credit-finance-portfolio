-- Q: What does the commercial book look like today, by sector and industry?
-- Skills: joins, aggregation, window function for share of total
WITH current_book AS (
    SELECT s.loan_id, s.outstanding, s.risk_grade, l.commitment, b.sector, b.industry
    FROM quarterly_snapshots s
    JOIN loans l     ON l.loan_id = s.loan_id
    JOIN borrowers b ON b.borrower_id = l.borrower_id
    WHERE s.as_of_date = '2026-09-30' AND s.outstanding > 0
)
SELECT sector,
       industry,
       COUNT(*)                                                        AS loans,
       ROUND(SUM(commitment) / 1e6, 1)                                 AS commitment_mm,
       ROUND(SUM(outstanding) / 1e6, 1)                                AS outstanding_mm,
       ROUND(100.0 * SUM(outstanding) / SUM(SUM(outstanding)) OVER (), 1) AS pct_of_book,
       ROUND(SUM(risk_grade * outstanding) / SUM(outstanding), 2)      AS wtd_avg_grade,
       ROUND(100.0 * SUM(CASE WHEN risk_grade >= 7 THEN outstanding ELSE 0 END) / SUM(outstanding), 1) AS criticized_pct
FROM current_book
GROUP BY sector, industry
ORDER BY outstanding_mm DESC;
