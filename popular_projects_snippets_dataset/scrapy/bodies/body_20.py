# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
self._stats[key] = min(self._stats.setdefault(key, value), value)
