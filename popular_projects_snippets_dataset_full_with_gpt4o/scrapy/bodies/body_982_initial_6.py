from twisted.internet.defer import inlineCallbacks, Deferred, succeed # pragma: no cover
from twisted.internet import reactor # pragma: no cover

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
