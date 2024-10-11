from twisted.internet.defer import Deferred, succeed # pragma: no cover
from twisted.internet.task import Clock # pragma: no cover
from twisted.internet.defer import inlineCallbacks # pragma: no cover

class Signals: # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback('done') # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class SignalsContainer: # pragma: no cover
    engine_stopped = 'engine_stopped' # pragma: no cover
 # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'signals': Signals(), # pragma: no cover
    'spider': MockSpider(), # pragma: no cover
    'running': True, # pragma: no cover
    '_closewait': Deferred(), # pragma: no cover
    'close_spider': lambda s, reason: succeed(None), # pragma: no cover
    'signals': Signals(), # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
signals = SignalsContainer() # pragma: no cover

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
