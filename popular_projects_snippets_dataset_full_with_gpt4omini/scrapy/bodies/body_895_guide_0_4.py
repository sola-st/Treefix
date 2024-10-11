from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class MockProtocolFactory: # pragma: no cover
    def buildProtocol(self, addr): # pragma: no cover
        return object() # pragma: no cover
protocolFactory = MockProtocolFactory() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
def connectDefer(): # pragma: no cover
    d = Deferred() # pragma: no cover
    reactor.callLater(0, d.callback, None)  # Simulate async success # pragma: no cover
    return d # pragma: no cover
super = type('MockSuper', (object,), {'connect': connectDefer})() # pragma: no cover
def requestTunnel(result): # pragma: no cover
    print('Tunnel requested') # pragma: no cover
self.requestTunnel = requestTunnel # pragma: no cover
def connectFailed(failure): # pragma: no cover
    print('Connection failed') # pragma: no cover
self.connectFailed = connectFailed # pragma: no cover

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
