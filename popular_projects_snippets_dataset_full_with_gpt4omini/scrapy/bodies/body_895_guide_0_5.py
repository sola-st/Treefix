from twisted.internet import defer # pragma: no cover
from twisted.internet import protocol # pragma: no cover

protocolFactory = protocol.Protocol() # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = defer.Deferred() # pragma: no cover
def connect(self, protocolFactory): return defer.Deferred() # pragma: no cover
setattr(Mock, 'connect', connect) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
self._protocolFactory = protocolFactory
_l_(9836)
connectDeferred = super().connect(protocolFactory)
_l_(9837)
connectDeferred.addCallback(self.requestTunnel)
_l_(9838)
connectDeferred.addErrback(self.connectFailed)
_l_(9839)
aux = self._tunnelReadyDeferred
_l_(9840)
exit(aux)
