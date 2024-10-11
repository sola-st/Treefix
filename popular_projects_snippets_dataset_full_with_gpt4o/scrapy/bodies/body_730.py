# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
if hasattr(self, '_crawler'):
    raise RuntimeError("crawler already set")
self._crawler = crawler
