-- Q: Quarter to quarter, how often do loans roll into worse delinquency buckets?
-- Skills: LAG() over a partition, transition counts
WITH b AS (
    SELECT loan_id, as_of_date,
           CASE WHEN nonaccrual = 1 OR days_past_due >= 90 THEN '4: 90+ / nonaccrual'
                WHEN days_past_due >= 30 THEN '3: 30-89'
                WHEN days_past_due >= 1  THEN '2: 1-29'
                ELSE '1: Current' END AS bucket
    FROM quarterly_snapshots
), t AS (
    SELECT loan_id, as_of_date, bucket,
           LAG(bucket) OVER (PARTITION BY loan_id ORDER BY as_of_date) AS prior_bucket
    FROM b
)
SELECT prior_bucket AS from_bucket,
       COUNT(*) AS loan_quarters,
       ROUND(100.0 * SUM(bucket = '1: Current') / COUNT(*), 2)          AS to_current_pct,
       ROUND(100.0 * SUM(bucket = '2: 1-29') / COUNT(*), 2)             AS to_1_29_pct,
       ROUND(100.0 * SUM(bucket = '3: 30-89') / COUNT(*), 2)            AS to_30_89_pct,
       ROUND(100.0 * SUM(bucket = '4: 90+ / nonaccrual') / COUNT(*), 2) AS to_90_plus_pct
FROM t
WHERE prior_bucket IS NOT NULL
GROUP BY prior_bucket
ORDER BY prior_bucket;
