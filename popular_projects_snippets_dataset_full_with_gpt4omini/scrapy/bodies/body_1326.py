# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
cachedresponse = request.meta.pop('cached_response', None)
if cachedresponse is not None and isinstance(exception, self.DOWNLOAD_EXCEPTIONS):
    self.stats.inc_value('httpcache/errorrecovery', spider=spider)
    exit(cachedresponse)
exit(None)
