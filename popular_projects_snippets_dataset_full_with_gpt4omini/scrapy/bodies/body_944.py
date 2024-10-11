# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
if self.waiting:
    self.waiting = 0
    self.deferred.errback(reason)
