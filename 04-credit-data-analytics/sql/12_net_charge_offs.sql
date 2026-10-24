-- Q: What are annual net charge-offs as a share of average loans outstanding?
-- Skills: aggregating snapshots by year, ratio of sums
SELECT substr(as_of_date, 1, 4)                         AS year,
       ROUND(SUM(charge_off) / 1e6, 2)                  AS charge_offs_mm,
       ROUND(AVG(q_out) / 1e6, 1)                       AS avg_outstanding_mm,
       ROUND(100.0 * SUM(charge_off) / AVG(q_out), 3)   AS nco_rate_pct
FROM (
    SELECT as_of_date, charge_off,
           SUM(outstanding) OVER (PARTITION BY as_of_date) AS q_out
    FROM quarterly_snapshots
)
GROUP BY year
ORDER BY year;
