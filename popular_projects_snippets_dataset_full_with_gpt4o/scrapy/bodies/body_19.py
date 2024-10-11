# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
self._stats[key] = max(self._stats.setdefault(key, value), value)
