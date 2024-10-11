from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.followRedirect = True # pragma: no cover
self.afterFoundGet = lambda: None # pragma: no cover
self.timeout = 5 # pragma: no cover
self.deferred = Mock() # pragma: no cover
self.deferred.addBoth = lambda func1, func2: None # pragma: no cover
self._cancelTimeout = lambda timeout: None # pragma: no cover
addr = ('127.0.0.1', 8080) # pragma: no cover
ClientFactory.buildProtocol = lambda self, addr: Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
from l3.Runtime import _l_
p = ClientFactory.buildProtocol(self, addr)
_l_(9883)
p.followRedirect = self.followRedirect
_l_(9884)
p.afterFoundGet = self.afterFoundGet
_l_(9885)
if self.timeout:
    _l_(9890)

    try:
        from twisted.internet import reactor
        _l_(9887)

    except ImportError:
        pass
    timeoutCall = reactor.callLater(self.timeout, p.timeout)
    _l_(9888)
    self.deferred.addBoth(self._cancelTimeout, timeoutCall)
    _l_(9889)
aux = p
_l_(9891)
exit(aux)
