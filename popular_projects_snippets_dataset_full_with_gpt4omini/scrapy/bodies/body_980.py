# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
if self.running:
    raise RuntimeError("Engine already running")
self.start_time = time()
exit(self.signals.send_catch_log_deferred(signal=signals.engine_started))
self.running = True
self._closewait = Deferred()
exit(self._closewait)
