#!/usr/bin/env python3
"""Search the knowledge library. Prints verbatim excerpts with citations. Exit 2 = nothing relevant found.

  python3 search.py "make a market adverse selection" [--firm optiver] [--kind paid-site] [--top 6]
  python3 search.py --exact "80 in 8" [--firm optiver]       # literal substring (case-insensitive)
  python3 search.py --show S3#14                              # print one full chunk
Firm filter includes 'general' sources too. Citation format used everywhere: [S3 p.12 #14].
"""
import argparse, json, math, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "library"))
from lib import *

ap = argparse.ArgumentParser()
ap.add_argument("query", nargs="?"); ap.add_argument("--firm"); ap.add_argument("--kind")
ap.add_argument("--top", type=int, default=6); ap.add_argument("--exact"); ap.add_argument("--show")
ap.add_argument("--chars", type=int, default=900)
a = ap.parse_args()
m = load_manifest(); meta = {s["id"]: s for s in m["sources"]}

def load(firm=None, kind=None):
    for s in m["sources"]:
        if firm and firm.lower() not in s["firm"] and "general" not in s["firm"]: continue
        if kind and s["kind"] != kind: continue
        for line in open(LIB / "chunks" / f"{s['id']}.jsonl"):
            yield json.loads(line)

def cite(c): return f"[{c['src']} {c['loc']} #{c['n']}]"
def head(c):
    s = meta[c["src"]]; return f"{cite(c)} {s['title']} | {s['kind']} | {s['origin'] or 'origin unknown'} | firms={','.join(s['firm'])}"

if a.show:
    sid, n = a.show.split("#")
    for c in load():
        if c["src"] == sid and c["n"] == int(n): print(head(c)); print(c["text"]); sys.exit()
    sys.exit("chunk not found")
if not m["sources"]:
    print("LIBRARY EMPTY: no sources ingested yet."); sys.exit(2)

chunks = list(load(a.firm, a.kind))
if a.exact:
    hits = [c for c in chunks if a.exact.lower() in c["text"].lower()]
    for c in hits[: a.top]:
        i = c["text"].lower().index(a.exact.lower()); lo = max(0, i - a.chars // 2)
        print(head(c)); print("   ..." + c["text"][lo: lo + a.chars].replace("\n", " ") + "...\n")
    print(f"{len(hits)} chunk(s) contain {a.exact!r}" + (f" (firm={a.firm}+general)" if a.firm else ""))
    sys.exit(0 if hits else 2)

q = tokens(a.query or "")
if not q: ap.error("query required")
docs = [(c, Counter(tokens(c["text"]))) for c in chunks]
N = len(docs) or 1; avg = sum(sum(t.values()) for _, t in docs) / N or 1
df = Counter(w for _, t in docs for w in set(t))
scored = []
for c, t in docs:
    dl = sum(t.values()); s = 0.0
    for w in set(q):
        if t[w]:
            idf = math.log(1 + (N - df[w] + .5) / (df[w] + .5))
            s += idf * t[w] * 2.2 / (t[w] + 1.2 * (0.25 + 0.75 * dl / avg))
    if s > 0: scored.append((s, c))
scored.sort(key=lambda x: -x[0])
matched = lambda c: len({w for w in q if w in c["text"].lower()})
scored = [(s, c) for s, c in scored if matched(c) >= max(1, len(set(q)) // 3)]
for s, c in scored[: a.top]:
    print(f"{head(c)}  score={s:.1f}"); print("   " + c["text"][: a.chars].replace("\n", " ") + ("..." if len(c["text"]) > a.chars else "") + "\n")
if not scored:
    print(f"NO RELEVANT PASSAGES in {len(chunks)} chunks" + (f" (firm={a.firm}+general)" if a.firm else "") +
          ". Do not answer from memory as if sourced; say it is not in the library."); sys.exit(2)
