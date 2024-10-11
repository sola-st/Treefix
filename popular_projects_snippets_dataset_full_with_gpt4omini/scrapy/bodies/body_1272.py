# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/downloadtimeout.py
self._timeout = getattr(spider, 'download_timeout', self._timeout)
