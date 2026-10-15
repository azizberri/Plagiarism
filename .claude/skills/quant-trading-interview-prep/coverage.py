#!/usr/bin/env python3
"""Map a folder of course documents onto the quant-trading interview taxonomy.

Usage:  python3 coverage.py <docs_dir> [--role trader|research] [--json out.json]

Reads .txt .md .tex .py .ipynb .pdf (needs pdftotext) .docx .pptx; stdlib only.
Prints, per topic: priority, keyword hits, which files hit, and a verdict:
  COVERED  - strong evidence your course material includes it (still verify depth)
  PARTIAL  - some mentions; probably intro level
  GAP      - no evidence in your documents
  N/A      - practice skill that documents cannot show (always needs deliberate practice)
Keyword hits show a topic APPEARS in your material, not that you mastered it.
"""
import argparse, json, os, re, subprocess, sys, zipfile
from pathlib import Path

HERE = Path(__file__).parent
TEXT_EXT = {".txt", ".md", ".tex", ".py", ".r", ".rmd", ".csv"}

def read_file(p: Path) -> str:
    ext = p.suffix.lower()
    try:
        if ext in TEXT_EXT:
            return p.read_text(errors="ignore")
        if ext == ".ipynb":
            nb = json.loads(p.read_text(errors="ignore"))
            return "\n".join("".join(c.get("source", [])) for c in nb.get("cells", []))
        if ext == ".pdf":
            r = subprocess.run(["pdftotext", "-q", str(p), "-"], capture_output=True, text=True, timeout=120)
            return r.stdout
        if ext in (".docx", ".pptx"):
            with zipfile.ZipFile(p) as z:
                names = [n for n in z.namelist() if n.endswith(".xml") and
                         (n.startswith("word/document") or n.startswith("ppt/slides/slide"))]
                xml = " ".join(z.read(n).decode("utf8", "ignore") for n in names)
            return re.sub(r"<[^>]+>", " ", xml)
    except Exception as e:  # unreadable file should not abort the scan
        print(f"warn: {p.name}: {e}", file=sys.stderr)
    return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docs_dir")
    ap.add_argument("--role", choices=["trader", "research"], default="trader")
    ap.add_argument("--json")
    a = ap.parse_args()

    topics = json.loads((HERE / "topics.json").read_text())["topics"]
    root = Path(a.docs_dir)
    files = [p for p in root.rglob("*") if p.is_file()]
    corpus = {}
    for p in files:
        t = read_file(p)
        if t.strip():
            corpus[str(p.relative_to(root))] = t.lower()
    skipped = len(files) - len(corpus)
    print(f"Scanned {len(corpus)} readable files ({skipped} unreadable/unsupported) in {root}\n")

    order = {"core": 0, "high": 1, "medium": 2, "low": 3}
    out = []
    for t in sorted(topics, key=lambda t: order[t["priority"]]):
        pri = t["priority"]
        if a.role == "research" and t["id"] in ("statistics", "linear-algebra-calculus", "stochastic-calculus", "ml-timeseries", "coding"):
            pri = "high"
        pats = [re.compile(k) for k in t["keywords"]]
        if not pats:  # skills that cannot be detected in documents (e.g. communication)
            out.append({"id": t["id"], "name": t["name"], "priority": pri, "verdict": "N/A", "hits": 0,
                        "distinct_keywords": 0, "files": {}, "note": t.get("note", "")})
            continue
        per_file, total, distinct = {}, 0, set()
        for f, txt in corpus.items():
            n = 0
            for pat in pats:
                m = len(pat.findall(txt))
                if m:
                    n += m; distinct.add(pat.pattern)
            if n:
                per_file[f] = n; total += n
        frac = len(distinct) / len(pats)
        verdict = "COVERED" if (frac >= 0.4 and total >= 15) else "PARTIAL" if total >= 3 else "GAP"
        out.append({"id": t["id"], "name": t["name"], "priority": pri, "verdict": verdict,
                    "hits": total, "distinct_keywords": len(distinct), "files": dict(sorted(per_file.items(), key=lambda x: -x[1])[:3]),
                    "note": t.get("note") or t.get("course_overlap", "")})
    for o in out:
        print(f"[{o['priority'].upper():6}] {o['verdict']:8} {o['name']}  (hits={o['hits']}, kw={o['distinct_keywords']})")
        for f, n in o["files"].items():
            print(f"           - {f} ({n})")
        if o["verdict"] != "COVERED" and o["note"]:
            print(f"           note: {o['note']}")
    print("\nPriority gaps (core/high that are GAP or PARTIAL):")
    for o in out:
        if o["priority"] in ("core", "high") and o["verdict"] not in ("COVERED", "N/A"):
            print(f"  * {o['name']} -> {o['verdict']}")
    if a.json:
        Path(a.json).write_text(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
