from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover

class MockSignals(object): # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        return succeed(None) # pragma: no cover
signals = MockSignals() # pragma: no cover
self = type('Mock', (object,), {'signals': signals, 'running': True, '_closewait': Deferred(), 'close_spider': lambda spider, reason: succeed(None), 'spider': 'mock_spider'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
"""Gracefully stop the execution engine"""
@inlineCallbacks
def _finish_stopping_engine(_) -> Deferred:
    _l_(6136)

    aux = self.signals.send_catch_log_deferred(signal=signals.engine_stopped)
    _l_(6134)
    exit(aux)
    self._closewait.callback(None)
    _l_(6135)

if not self.running:
    _l_(6138)

    raise RuntimeError("Engine not running")
    _l_(6137)

self.running = False
_l_(6139)
dfd = self.close_spider(self.spider, reason="shutdown") if self.spider is not None else succeed(None)
_l_(6140)
aux = dfd.addBoth(_finish_stopping_engine)
_l_(6141)
exit(aux)
