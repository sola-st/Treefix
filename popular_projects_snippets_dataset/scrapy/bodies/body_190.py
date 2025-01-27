# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
self.mindelay = self._min_delay(spider)
self.maxdelay = self._max_delay(spider)
spider.download_delay = self._start_delay(spider)
