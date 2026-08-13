#!/usr/bin/env python3
"""Generate a sample weekly ops memo from the sample CSV."""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_config():
    cfg_path = ROOT / "config.example.yaml"
    try:
        import yaml

        return yaml.safe_load(cfg_path.read_text()) or {}
    except Exception:
        return {}


def read_metrics(csv_path: Path):
    rows = []
    with csv_path.open(newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def main() -> int:
    cfg = load_config() or {}
    cols = cfg.get("metric_columns", {})
    rev_col = cols.get("revenue", "revenue")
    signups_col = cols.get("new_signups", "signups")
    users_col = cols.get("active_users", "active_users")
    anom = cfg.get("anomaly", {})

    csv_path = ROOT / "_data" / "metrics.csv"
    if not csv_path.exists():
        print("missing _data/metrics.csv", file=sys.stderr)
        return 1
    rows = read_metrics(csv_path)

    # take last two rows as current vs prior
    current = rows[-1]
    prior = rows[-2]

    def num(row, col):
        raw = (row.get(col) or "0").replace("$", "").replace("₹", "").replace(",", "").strip()
        try:
            return float(raw)
        except ValueError:
            return 0.0

    rev_c, rev_p = num(current, rev_col), num(prior, rev_col)
    sig_c, sig_p = num(current, signups_col), num(prior, signups_col)
    usr_c = num(current, users_col)

    def pct(c, p):
        return ((c - p) / p * 100) if p else 0.0

    rev_d = pct(rev_c, rev_p)
    sig_d = pct(sig_c, sig_p)

    flags = []
    if rev_d <= float(anom.get("revenue_drop_pct", -20)):
        flags.append(f"🚩 Revenue: {rev_d:.1f}% (₹{rev_p:.0f} → ₹{rev_c:.0f}) — investigate")
    if rev_d >= float(anom.get("revenue_spike_pct", 50)):
        flags.append(f"🚩 Revenue spike: +{rev_d:.1f}% (₹{rev_p:.0f} → ₹{rev_c:.0f}) — investigate")
    if sig_d <= float(anom.get("signups_drop_pct", -30)):
        flags.append(f"🚩 Signups: {sig_d:.1f}% ({sig_p:.0f} → {sig_c:.0f}) — investigate")

    memo = f"""# Weekly Ops Memo

## Summary
Revenue was ₹{rev_c:,.0f} ({rev_d:+.1f}% WoW). Signups {sig_c:,.0f} ({sig_d:+.1f}% WoW), {usr_c:,.0f} active users.

## Metrics
| metric | current | prior | delta | delta% |
|--------|---------|-------|-------|--------|
| Revenue | ₹{rev_c:,.0f} | ₹{rev_p:,.0f} | {rev_c-rev_p:+,.0f} | {rev_d:+.1f}% |
| Signups | {sig_c:,.0f} | {sig_p:,.0f} | {sig_c-sig_p:+,.0f} | {sig_d:+.1f}% |
| Active users | {usr_c:,.0f} | — | — | — |

## Anomalies
{chr(10).join(flags) if flags else 'No anomalies flagged this week.'}

## Action Items
- [ ] Review {('revenue' if flags else 'growth')} trend — owner: TBD · due: this week · prio: P0
"""
    out = ROOT / "_data" / "weekly-memo-sample.md"
    out.write_text(memo, encoding="utf-8")
    print(f"Wrote {out}")
    print(memo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
