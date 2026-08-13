# Overview

The **Weekly Founder Ops Report Agent** turns scattered metrics into a board-ready weekly memo: intake → narrative → anomaly flags → action items. No hosted dashboard, no BI team.

## Weekly ritual
1. Export metrics to CSV (Stripe, Recurly, ads, product analytics).
2. Save as `_data/metrics.csv` (last two rows = current & prior week).
3. Run `python scripts/sample_memo.py`.
4. Review / share the memo; assign action items.

## Files
- `skills/` — 4 agent skills
- `prompts/` — ready prompts
- `scripts/sample_memo.py` — CSV → memo engine
- `_data/` — sample input + output
- `docs/` — schema + anomaly playbook
