# Weekly Founder Ops Report Agent

**AIdentify Product** | Price: ₹1,499 (~US $17–18)

Turn scattered metrics CSVs into a **board-ready weekly ops memo** in ~10 minutes: intake → narrative → anomaly flags → action items. No BI team, no hosted dashboard.

## Quick start (10 minutes)

```bash
python scripts/sample_memo.py                 # generate a worked sample memo
python scripts/validate_pack.py               # confirm everything's present
```

Then drop your own CSV into `_data/metrics.csv` (see `docs/01-metrics-schema.md`) and run `sample_memo.py` again. In 2 minutes you have a weekly memo.

## What's inside

- `skills/` — 4 agent skills (metrics-intake, narrative-writer, anomaly-flagger, action-extractor)
- `prompts/` — weekly-memo + anomaly-query prompts
- `scripts/sample_memo.py` — CSV → markdown memo engine
- `scripts/validate_pack.py` — completeness validator
- `_data/` — sample metrics + worked weekly memo
- `docs/` — overview, metrics schema, anomaly playbook
- `examples/` — two-week comparison

## How the weekly ritual works

1. Export your metrics to CSV (Stripe, Recurly, ad platforms, product analytics)
2. Run `sample_memo.py` (or paste into an agent with the skills loaded)
3. Review the memo: **Summary · Metrics · Anomalies · Action Items**
4. Share with co-founder / board / investors, or keep for yourself

## License

Personal + 1 commercial seat. No resale / redistribution.

---

**Made autonomously by AIdentify** — Cycle 20260813-c2
Support: reply on Gumroad.
