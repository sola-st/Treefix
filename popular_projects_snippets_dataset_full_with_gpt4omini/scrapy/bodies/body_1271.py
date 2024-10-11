# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/downloadtimeout.py
o = cls(crawler.settings.getfloat('DOWNLOAD_TIMEOUT'))
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
exit(o)
