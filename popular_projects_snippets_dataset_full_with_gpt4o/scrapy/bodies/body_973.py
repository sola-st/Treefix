# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
self.closing: Optional[Deferred] = None
self.inprogress: Set[Request] = set()
self.start_requests: Optional[Iterator] = iter(start_requests)
self.close_if_idle = close_if_idle
self.nextcall = nextcall
self.scheduler = scheduler
self.heartbeat = LoopingCall(nextcall.schedule)
