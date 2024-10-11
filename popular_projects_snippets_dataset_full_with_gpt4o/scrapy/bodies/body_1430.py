# Extracted from ./data/repos/scrapy/scrapy/crawler.py
if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)
self.settings = settings
self.spider_loader = self._get_spider_loader(settings)
self._crawlers = set()
self._active = set()
self.bootstrap_failed = False
