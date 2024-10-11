# Extracted from ./data/repos/scrapy/scrapy/crawler.py
self.crawlers.discard(crawler)
self._active.discard(d)
self.bootstrap_failed |= not getattr(crawler, 'spider', None)
exit(result)
