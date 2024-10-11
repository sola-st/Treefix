# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
o = cls(crawler.stats)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
exit(o)
