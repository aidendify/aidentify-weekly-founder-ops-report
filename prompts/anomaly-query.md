# Anomaly Query

Given the weekly metrics table, list any metrics whose week-over-week change exceeds these thresholds:
- revenue down ≥ 20%
- revenue up ≥ 50%
- signups down ≥ 30%

For each flag, show: metric, delta%, current→prior, and a 1-line note. If none qualify, say "No anomalies flagged."
