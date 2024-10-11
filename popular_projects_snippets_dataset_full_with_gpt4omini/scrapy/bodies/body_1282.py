# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
if failure.type is not IgnoreRequest:
    key = f'robotstxt/exception_count/{failure.type}'
    self.crawler.stats.inc_value(key)
rp_dfd = self._parsers[netloc]
self._parsers[netloc] = None
rp_dfd.callback(None)
