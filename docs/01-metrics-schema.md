# Metrics Schema — Weekly Founder Ops Report

The engine expects a CSV. Configure column names in `config.example.yaml`.

## Expected columns (configurable)
| Config key | Default column | Meaning |
|------------|----------------|---------|
| `revenue` | `revenue` | Weekly revenue (currency-agnostic; strips ₹/$/,) |
| `active_users` | `active_users` | Active users current period |
| `new_signups` | `signups` | New signups |
| `churn` | `churn` | (optional) churn |

## Row convention
- The **last two rows** are treated as **current** and **prior** week for WoW deltas.
- A `period` / `date` column is optional but recommended.

## Mapping your data
If your export uses different names, edit `config.example.yaml` `metric_columns` to point at your header names.
