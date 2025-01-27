# Extracted from ./data/repos/scrapy/scrapy/crawler.py
d = self.stop()
d.addBoth(self._stop_reactor)
exit(d)
