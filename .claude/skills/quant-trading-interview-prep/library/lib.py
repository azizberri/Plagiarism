"""Shared helpers for the knowledge library (stdlib only). Imported by ingest.py / search.py / progress.py."""
import hashlib, html, json, re, subprocess, zipfile
from pathlib import Path

LIB = Path(__file__).parent
MANIFEST = LIB / "manifest.json"

def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"next_id": 1, "sources": []}

def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=1, ensure_ascii=False))

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def strip_html(t: str) -> str:
    t = re.sub(r"(?is)<(script|style|nav|footer|svg)[^>]*>.*?</\1>", "", t)
    t = re.sub(r"(?i)<(br|/p|/h\d|/li|/tr|/div)[^>]*>", "\n", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))

def extract(p: Path):
    """Return list of (location_label, text) units, or None if unreadable."""
    ext = p.suffix.lower()
    try:
        if ext == ".pdf":
            out = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=300).stdout
            pages = out.split("\f")
            units = [(f"p.{i+1}", t) for i, t in enumerate(pages) if t.strip()]
            return units or None  # image-only PDF -> None
        if ext in (".docx", ".pptx"):
            with zipfile.ZipFile(p) as z:
                if ext == ".docx":
                    xml = z.read("word/document.xml").decode("utf8", "ignore")
                    xml = re.sub(r"</w:p>", "\n", xml)
                    return [("doc", re.sub(r"<[^>]+>", " ", xml))]
                slides = sorted((n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
                                key=lambda n: int(re.findall(r"\d+", n)[0]))
                return [(f"slide {re.findall(r'\d+', n)[0]}", re.sub(r"<[^>]+>", " ", z.read(n).decode("utf8", "ignore")))
                        for n in slides] or None
        if ext == ".ipynb":
            nb = json.loads(p.read_text(errors="ignore"))
            return [(f"cell {i+1}", "".join(c.get("source", []))) for i, c in enumerate(nb.get("cells", []))]
        if ext in (".html", ".htm"):
            return [("page", strip_html(p.read_text(errors="ignore")))]
        if ext in (".txt", ".md", ".tex", ".csv", ".json", ".py", ".r", ".rmd", ".log"):
            return [("text", p.read_text(errors="ignore"))]
    except Exception:
        return None
    return None  # unsupported (images, video, ...)

def chunk(units, target=220):
    """Split into ~target-word chunks on paragraph boundaries. Returns list of {loc, text}."""
    chunks = []
    for loc, text in units:
        text = re.sub(r"[ \t]+", " ", text)
        paras = [q.strip() for q in re.split(r"\n\s*\n", text) if q.strip()]
        buf, words = [], 0
        for q in paras:
            w = len(q.split())
            if buf and words + w > target:
                chunks.append({"loc": loc, "text": "\n".join(buf)}); buf, words = [], 0
            buf.append(q); words += w
        if buf:
            chunks.append({"loc": loc, "text": "\n".join(buf)})
    return chunks

def tokens(s: str):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", s.lower())
