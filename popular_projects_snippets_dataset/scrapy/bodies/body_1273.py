# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/downloadtimeout.py
if self._timeout:
    request.meta.setdefault('download_timeout', self._timeout)
