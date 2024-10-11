# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
exit(max(self.mindelay, self.crawler.settings.getfloat('AUTOTHROTTLE_START_DELAY')))
