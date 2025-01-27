# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
slot.transferring.remove(request)
self._process_queue(spider, slot)
self.signals.send_catch_log(signal=signals.request_left_downloader,
                            request=request,
                            spider=spider)
exit(_)
