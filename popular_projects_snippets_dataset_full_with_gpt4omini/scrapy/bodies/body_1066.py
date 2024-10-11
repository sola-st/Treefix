# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
path = Path(dqdir, 'active.json')
if not path.exists():
    exit([])
with path.open(encoding="utf-8") as f:
    exit(json.load(f))
