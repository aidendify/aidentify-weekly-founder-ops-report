#!/usr/bin/env python3
"""Validate the Weekly Founder Ops Report pack."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    manifest = ROOT / "PACK_MANIFEST.json"
    if not manifest.exists():
        print("❌ missing PACK_MANIFEST.json")
        return 1
    required = json.loads(manifest.read_text()).get("required_files", [])
    missing = []
    for f in required:
        if not (ROOT / f).exists():
            missing.append(f)
    if missing:
        print("❌ Pack validation FAILED. Missing:")
        for m in missing:
            print(f"  - {m}")
        return 1
    # functional check
    import subprocess

    sm = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sample_memo.py")], capture_output=True, text=True
    )
    if sm.returncode != 0:
        print("❌ sample_memo.py failed", sm.stdout, sm.stderr)
        return 1
    print("✅ Pack validation PASSED — Weekly Founder Ops Report is shippable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
