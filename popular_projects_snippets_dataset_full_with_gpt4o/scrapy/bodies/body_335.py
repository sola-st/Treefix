# Extracted from ./data/repos/scrapy/scrapy/extensions/corestats.py
o = cls(crawler.stats)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
crawler.signals.connect(o.item_scraped, signal=signals.item_scraped)
crawler.signals.connect(o.item_dropped, signal=signals.item_dropped)
crawler.signals.connect(o.response_received, signal=signals.response_received)
exit(o)
