# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http10.py
"""Return a deferred for the HTTP download"""
factory = self.HTTPClientFactory(request)
self._connect(factory)
exit(factory.deferred)
