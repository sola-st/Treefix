from twisted.internet.defer import Deferred, inlineCallbacks, succeed # pragma: no cover
from typing import Callable, Any, Optional # pragma: no cover

class signals: engine_stopped = 'engine_stopped' # pragma: no cover
class Mock: send_catch_log_deferred: Callable[[str], Deferred] = lambda self, signal: Deferred() # pragma: no cover
self = type('Engine', (object,), {'signals': Mock(), 'running': True, 'close_spider': lambda spider, reason: Deferred(), 'spider': type('Spider', (object,), {})(), '_closewait': Deferred()}) # pragma: no cover
exit = lambda x: None # pragma: no cover

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
