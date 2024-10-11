# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
if self.closing is not None and not self.inprogress:
    if self.nextcall:
        self.nextcall.cancel()
        if self.heartbeat.running:
            self.heartbeat.stop()
    self.closing.callback(None)
