from twisted.internet.defer import Deferred, inlineCallbacks, succeed # pragma: no cover

class MockEngine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.running = True # pragma: no cover
        self.spider = 'mock_spider' # pragma: no cover
 # pragma: no cover
    def close_spider(self, spider, reason): # pragma: no cover
        return succeed(None) # pragma: no cover
 # pragma: no cover
    @property # pragma: no cover
    def signals(self): # pragma: no cover
        class Signals: # pragma: no cover
            def send_catch_log_deferred(self, signal): # pragma: no cover
                return Deferred() # pragma: no cover
        return Signals() # pragma: no cover
 # pragma: no cover
    @property # pragma: no cover
    def _closewait(self): # pragma: no cover
        class CloseWait: # pragma: no cover
            def callback(self, _): # pragma: no cover
                pass # pragma: no cover
        return CloseWait() # pragma: no cover
 # pragma: no cover
mock_engine = MockEngine() # pragma: no cover
# Bind the mock_engine methods and attributes to the global references # pragma: no cover
self = mock_engine # pragma: no cover

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
