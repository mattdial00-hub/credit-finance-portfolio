-- Q: Who are the 20 largest relationships, and how concentrated is the book?
-- Skills: CTE, RANK(), running total with SUM() OVER (ORDER BY ...)
WITH rel AS (
    SELECT b.borrower_id, b.name, b.industry,
           SUM(l.commitment)  AS commitment,
           SUM(s.outstanding) AS outstanding,
           MAX(s.risk_grade)  AS worst_grade
    FROM loans l
    JOIN borrowers b ON b.borrower_id = l.borrower_id
    JOIN quarterly_snapshots s ON s.loan_id = l.loan_id AND s.as_of_date = '2026-09-30'
    GROUP BY b.borrower_id
), ranked AS (
    SELECT *,
           RANK() OVER (ORDER BY commitment DESC)                          AS rnk,
           SUM(commitment) OVER (ORDER BY commitment DESC)                 AS running_commit,
           SUM(commitment) OVER ()                                         AS total_commit
    FROM rel
)
SELECT rnk, name, industry,
       ROUND(commitment / 1e6, 2)                       AS commitment_mm,
       ROUND(outstanding / 1e6, 2)                      AS outstanding_mm,
       worst_grade,
       ROUND(100.0 * commitment / total_commit, 2)      AS pct_of_total,
       ROUND(100.0 * running_commit / total_commit, 1)  AS cumulative_pct
FROM ranked
WHERE rnk <= 20
ORDER BY rnk;
