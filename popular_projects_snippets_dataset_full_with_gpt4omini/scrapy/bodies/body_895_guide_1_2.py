from twisted.internet import defer # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol):# pragma: no cover
    def requestTunnel(self):# pragma: no cover
        print('Tunnel requested')# pragma: no cover
    def connectFailed(self, error):# pragma: no cover
        print('Connection failed:', error) # pragma: no cover
protocolFactory = MockProtocol() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = defer.Deferred() # pragma: no cover
def connect(self, protocolFactory):# pragma: no cover
    d = defer.Deferred()# pragma: no cover
    reactor.callLater(0, d.callback, None)  # Simulate async success# pragma: no cover
    return d # pragma: no cover
super = type('MockSuper', (object,), {'connect': connect})() # pragma: no cover

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
