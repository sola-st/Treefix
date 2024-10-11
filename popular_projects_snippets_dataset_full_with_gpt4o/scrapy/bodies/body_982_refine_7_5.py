from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover
from types import SimpleNamespace # pragma: no cover

inlineCallbacks = inlineCallbacks # pragma: no cover
Deferred = Deferred # pragma: no cover
self = SimpleNamespace() # pragma: no cover
signals = SimpleNamespace(engine_stopped='engine_stopped') # pragma: no cover
self.signals = signals # pragma: no cover
self._closewait = Deferred() # pragma: no cover
self.running = True # pragma: no cover
self.close_spider = lambda spider, reason: succeed(None) # pragma: no cover

from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover

class Signals: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.engine_stopped = 'engine_stopped' # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class MockCloseWait: # pragma: no cover
    def callback(self, arg): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockEngine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.signals = Signals() # pragma: no cover
        self._closewait = MockCloseWait() # pragma: no cover
        self.running = True # pragma: no cover
        self.spider = type('Spider', (object,), {})() # pragma: no cover
    def close_spider(self, spider, reason): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
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
