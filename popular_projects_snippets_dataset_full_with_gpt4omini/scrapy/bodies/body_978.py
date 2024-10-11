# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
self.crawler = crawler
self.settings = crawler.settings
self.signals = crawler.signals
self.logformatter = crawler.logformatter
self.slot: Optional[Slot] = None
self.spider: Optional[Spider] = None
self.running = False
self.paused = False
self.scheduler_cls = self._get_scheduler_class(crawler.settings)
downloader_cls = load_object(self.settings['DOWNLOADER'])
self.downloader = downloader_cls(crawler)
self.scraper = Scraper(crawler)
self._spider_closed_callback = spider_closed_callback
