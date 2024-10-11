from twisted.internet.defer import Deferred, succeed # pragma: no cover
from twisted.internet.task import deferLater # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from twisted.internet.defer import inlineCallbacks # pragma: no cover
import signals # pragma: no cover
import logging # pragma: no cover

class MockSignals: # pragma: no cover
    def send_catch_log_deferred(self, signal): # pragma: no cover
        dfd = Deferred() # pragma: no cover
        logging.info(f'Signal {signal} caught and logged.') # pragma: no cover
        reactor.callLater(1, dfd.callback, None) # pragma: no cover
        return dfd # pragma: no cover
 # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Engine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.signals = MockSignals() # pragma: no cover
        self._closewait = Deferred() # pragma: no cover
        self.running = True # pragma: no cover
        self.spider = MockSpider() # pragma: no cover
 # pragma: no cover
    def close_spider(self, spider, reason): # pragma: no cover
        logging.info(f'Spider closed due to {reason}.') # pragma: no cover
        return deferLater(reactor, 1, lambda: None) # pragma: no cover
 # pragma: no cover
engine = Engine() # pragma: no cover
 # pragma: no cover

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
