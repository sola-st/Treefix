# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
if result is not None:
    exit(result)
if self.download_func:
    # this ugly code was left only to support tests. TODO: remove
    dfd = mustbe_deferred(self.download_func, request, info.spider)
    dfd.addCallbacks(
        callback=self.media_downloaded, callbackArgs=(request, info), callbackKeywords={'item': item},
        errback=self.media_failed, errbackArgs=(request, info))
else:
    self._modify_media_request(request)
    dfd = self.crawler.engine.download(request)
    dfd.addCallbacks(
        callback=self.media_downloaded, callbackArgs=(request, info), callbackKeywords={'item': item},
        errback=self.media_failed, errbackArgs=(request, info))
exit(dfd)
