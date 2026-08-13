# Metrics Intake

**Role**: Turn raw CSV into normalized weekly metrics.

## Input
Path to a CSV (columns configurable in config.example.yaml) or pasted rows.

## Steps
1. Map configured column names (revenue, active_users, signups, churn) to actual CSV header.
2. Normalize numbers (strip ₹/$/commas), convert currency display.
3. Compute deltas vs previous period when a `period` or date column is present.
4. Output a normalized table: metric | current | prior | delta | delta%.

## Output format
```markdown
| metric | current | prior | delta | delta% |
|--------|---------|-------|-------|--------|
```

## Notes
- Missing columns → output "not_supplied" and keep going.
- Never invent numbers.
