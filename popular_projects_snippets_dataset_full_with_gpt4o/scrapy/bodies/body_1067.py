# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
with Path(dqdir, 'active.json').open('w', encoding="utf-8") as f:
    json.dump(state, f)
