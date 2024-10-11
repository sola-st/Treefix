from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover
from typing import Any # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self.signals = type('MockSignals', (object,), {})() # pragma: no cover
signals = type('MockSignalsEnum', (object,), {'engine_stopped': 'engine_stopped_signal'})() # pragma: no cover
self._closewait = Deferred() # pragma: no cover
self.running = True # pragma: no cover
def mock_close_spider(spider: Any, reason: str) -> Deferred: return succeed(None) # pragma: no cover
self.close_spider = mock_close_spider # pragma: no cover
self.spider = type('MockSpider', (object,), {})() # pragma: no cover
self.signals.send_catch_log_deferred = lambda signal: succeed(None) # pragma: no cover

from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover
from twisted.internet.task import react # pragma: no cover

class MockEngine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.signals = self.MockSignals() # pragma: no cover
        self._closewait = Deferred() # pragma: no cover
        self.running = True # pragma: no cover
        self.spider = self.MockSpider() # pragma: no cover
    def close_spider(self, spider, reason): # pragma: no cover
        print(f"Closing spider: {spider}, Reason: {reason}") # pragma: no cover
        return succeed('Spider closed') # pragma: no cover
    class MockSignals: # pragma: no cover
        engine_stopped = 'engine_stopped' # pragma: no cover
        def send_catch_log_deferred(self, signal): # pragma: no cover
            print(f"Signal sent: {signal}") # pragma: no cover
            return succeed(None) # pragma: no cover
    class MockSpider: # pragma: no cover
        pass # pragma: no cover
self = MockEngine() # pragma: no cover
signals = self.signals # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
"""Gracefully stop the execution engine"""
@inlineCallbacks
def _finish_stopping_engine(_) -> Deferred:
    _l_(17506)

    aux = self.signals.send_catch_log_deferred(signal=signals.engine_stopped)
    _l_(17504)
    exit(aux)
    self._closewait.callback(None)
    _l_(17505)

if not self.running:
    _l_(17508)

    raise RuntimeError("Engine not running")
    _l_(17507)

self.running = False
_l_(17509)
dfd = self.close_spider(self.spider, reason="shutdown") if self.spider is not None else succeed(None)
_l_(17510)
aux = dfd.addBoth(_finish_stopping_engine)
_l_(17511)
exit(aux)
