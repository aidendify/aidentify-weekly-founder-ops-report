# Anomaly Playbook — Weekly Founder Ops Report

Anomalies are computed as week-over-week deltas against default thresholds in `config.example.yaml`:
- Revenue down ≥ 20% → flag
- Revenue up ≥ 50% → flag
- Signups down ≥ 30% → flag

## When flagged
1. Name the metric and the % change.
2. Give a 1-line plausible cause **only if you have evidence**; otherwise "investigate".
3. Add an action item to dig in.

## Adjusting thresholds
Edit `config.example.yaml` `anomaly:` block for your business (e.g. a seasonal business may want tighter/looser bands).
