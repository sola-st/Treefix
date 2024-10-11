from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class MockSignals: # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        return succeed('Engine stopped') # pragma: no cover
 # pragma: no cover
signals = type('MockSignalsEnum', (object,), {'engine_stopped': 'engine_stopped'}) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'signals': MockSignals(), '_closewait': Deferred(), 'running': True, 'close_spider': lambda spider, reason: succeed('Spider closed'), 'spider': 'mock_spider'})() # pragma: no cover

from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover

class MockSignals: # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        return succeed('Engine stopped') # pragma: no cover
 # pragma: no cover
signals = type('MockSignalsEnum', (object,), {'engine_stopped': 'engine_stopped'}) # pragma: no cover
 # pragma: no cover
def mock_close_spider(spider, reason): # pragma: no cover
    if spider is None: # pragma: no cover
        return succeed(None) # pragma: no cover
    return succeed(f'simulated close_spider call with reason: {reason}') # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'signals': MockSignals(), # pragma: no cover
    '_closewait': Deferred(), # pragma: no cover
    'running': True, # pragma: no cover
    'close_spider': mock_close_spider, # pragma: no cover
    'spider': None # pragma: no cover
})() # pragma: no cover

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
