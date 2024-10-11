# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
self.signals.send_catch_log(signals.request_scheduled, request=request, spider=spider)
if not self.slot.scheduler.enqueue_request(request):  # type: ignore[union-attr]
    self.signals.send_catch_log(signals.request_dropped, request=request, spider=spider)
