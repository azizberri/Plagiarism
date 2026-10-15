#!/usr/bin/env python3
"""Persistent study log so a new chat remembers where the user is.

  python3 progress.py add --topic probability --firm optiver --score 7/10 --note "missed gambler's ruin setup"
  python3 progress.py show [--firm optiver]
Stored in library/progress.jsonl (commit it). Only record things the user actually did or said."""
import argparse, json, time
from pathlib import Path
P = Path(__file__).parent / "library" / "progress.jsonl"
ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["add", "show"])
ap.add_argument("--topic"); ap.add_argument("--firm"); ap.add_argument("--score", default=""); ap.add_argument("--note", default="")
a = ap.parse_args()
if a.cmd == "add":
    if not a.topic: ap.error("--topic required")
    with open(P, "a") as f: f.write(json.dumps({"date": time.strftime("%Y-%m-%d"), "topic": a.topic, "firm": a.firm or "general", "score": a.score, "note": a.note}) + "\n")
    print("logged")
else:
    rows = [json.loads(l) for l in open(P)] if P.exists() else []
    if a.firm: rows = [r for r in rows if r["firm"] in (a.firm, "general")]
    for r in rows: print(f"{r['date']}  {r['firm']:<12} {r['topic']:<24} {r['score']:<7} {r['note']}")
    print(f"{len(rows)} entries" if rows else "no progress logged yet")
