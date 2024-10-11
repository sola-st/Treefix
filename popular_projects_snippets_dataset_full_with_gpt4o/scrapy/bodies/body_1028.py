# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
self.slot: Optional[Slot] = None
self.spidermw = SpiderMiddlewareManager.from_crawler(crawler)
itemproc_cls = load_object(crawler.settings['ITEM_PROCESSOR'])
self.itemproc = itemproc_cls.from_crawler(crawler)
self.concurrent_items = crawler.settings.getint('CONCURRENT_ITEMS')
self.crawler = crawler
self.signals = crawler.signals
self.logformatter = crawler.logformatter
