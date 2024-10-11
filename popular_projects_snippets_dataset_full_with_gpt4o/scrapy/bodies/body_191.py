# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
s = self.crawler.settings
exit(getattr(spider, 'download_delay', s.getfloat('DOWNLOAD_DELAY')))
