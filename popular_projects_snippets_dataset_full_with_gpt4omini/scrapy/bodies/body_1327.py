# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
if self.policy.should_cache_response(response, request):
    self.stats.inc_value('httpcache/store', spider=spider)
    self.storage.store_response(spider, request, response)
else:
    self.stats.inc_value('httpcache/uncacheable', spider=spider)
