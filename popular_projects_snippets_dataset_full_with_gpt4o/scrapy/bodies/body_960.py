# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
key, slot = self._get_slot(request, spider)
request.meta[self.DOWNLOAD_SLOT] = key

def _deactivate(response):
    slot.active.remove(request)
    exit(response)

slot.active.add(request)
self.signals.send_catch_log(signal=signals.request_reached_downloader,
                            request=request,
                            spider=spider)
deferred = defer.Deferred().addBoth(_deactivate)
slot.queue.append((request, deferred))
self._process_queue(spider, slot)
exit(deferred)
