#!/usr/bin/env python3
"""Add documents to the persistent knowledge library.

  python3 ingest.py <file-or-dir> --firm optiver,imc|general --kind book|course|forum|paid-site|official|notes --origin "tradinginterview.com (paid)"
  python3 ingest.py --list
  python3 ingest.py --remove S12

Originals are copied to library/sources/<firm>/ ; text chunks go to library/chunks/<id>.jsonl; library/manifest.json is
the index. Re-ingesting an identical file (same sha256) is skipped. Files that cannot be read (image-only PDFs, screenshots,
video, unknown types) are REPORTED, never silently dropped: the library only contains what was really extracted.
"""
import argparse, json, shutil, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "library"))
from lib import *

ap = argparse.ArgumentParser()
ap.add_argument("path", nargs="?")
ap.add_argument("--firm", default="general", help="comma-separated slugs, e.g. optiver,imc ; 'general' for firm-independent material")
ap.add_argument("--kind", default="notes", choices=["book", "course", "forum", "paid-site", "official", "notes", "video-transcript", "other"])
ap.add_argument("--origin", default="", help="where it came from (site/book/course name); required for provenance")
ap.add_argument("--list", action="store_true"); ap.add_argument("--remove")
a = ap.parse_args()
m = load_manifest()

if a.list:
    for s in m["sources"]:
        print(f"{s['id']:>5}  {s['kind']:<16} firms={','.join(s['firm']):<22} chunks={s['chunks']:<4} {s['title']}  <{s['origin'] or 'origin unknown'}>")
    print(f"{len(m['sources'])} sources"); sys.exit()
if a.remove:
    s = next((x for x in m["sources"] if x["id"] == a.remove), None)
    if not s: sys.exit("no such id")
    (LIB / "chunks" / f"{s['id']}.jsonl").unlink(missing_ok=True); (LIB / s["file"]).unlink(missing_ok=True)
    m["sources"].remove(s); save_manifest(m); print("removed", a.remove); sys.exit()
if not a.path: ap.error("path required")

root = Path(a.path)
files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file() and not p.name.startswith("."))
firms = [f.strip().lower() for f in a.firm.split(",") if f.strip()]
seen = {s["sha256"] for s in m["sources"]}
added, skipped, dup = [], [], []
for p in files:
    h = sha256(p)
    if h in seen:
        dup.append(p.name); continue
    units = extract(p)
    if not units:
        skipped.append(p.name); continue
    chunks = chunk(units)
    if not chunks:
        skipped.append(p.name); continue
    sid = f"S{m['next_id']}"; m["next_id"] += 1
    dest = LIB / "sources" / firms[0] / f"{sid}_{p.name}"
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, dest)
    with open(LIB / "chunks" / f"{sid}.jsonl", "w") as f:
        for i, c in enumerate(chunks, 1):
            f.write(json.dumps({"src": sid, "n": i, **c}, ensure_ascii=False) + "\n")
    m["sources"].append({"id": sid, "title": p.stem, "file": str(dest.relative_to(LIB)), "kind": a.kind, "origin": a.origin,
                         "firm": firms, "sha256": h, "chunks": len(chunks), "added": time.strftime("%Y-%m-%d")})
    seen.add(h); added.append(f"{sid} {p.name} ({len(chunks)} chunks)")
save_manifest(m)
print("added:", *added, sep="\n  " if added else " ") if added else print("added: none")
if dup: print("duplicates skipped:", ", ".join(dup))
if skipped:
    print("NOT INGESTED (unreadable: image-only PDF, screenshot, video or unsupported type) - nothing from these is in the library:")
    for s in skipped: print("  -", s)
    print("  Fix: paste the text, export to text/PDF with a text layer, or send a transcript.")
if not a.origin: print("warning: no --origin given; provenance will show 'origin unknown'")
