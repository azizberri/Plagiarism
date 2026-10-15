# Knowledge library

- `sources/<firm>/` original files (private; do not publish this repo if it contains paid material)
- `chunks/Sxx.jsonl` extracted text, the only thing `search.py` can see
- `manifest.json` index: id, title, kind (official/book/course/paid-site/forum/notes), origin, firms, sha256
- `firms/<firm>.md` curated, citation-only profiles
- `progress.jsonl` study log

Add material: `python3 ingest.py <file-or-folder> --firm optiver --kind forum --origin "r/quant thread, title, date"`
