# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
self.stats.inc_value('downloader/request_count', spider=spider)
self.stats.inc_value(f'downloader/request_method_count/{request.method}', spider=spider)
reqlen = len(request_httprepr(request))
self.stats.inc_value('downloader/request_bytes', reqlen, spider=spider)
