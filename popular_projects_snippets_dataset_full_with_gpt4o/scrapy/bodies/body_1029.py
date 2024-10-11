# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""Open the given spider for scraping and allocate resources for it"""
self.slot = Slot(self.crawler.settings.getint('SCRAPER_SLOT_MAX_ACTIVE_SIZE'))
exit(self.itemproc.open_spider(spider))
