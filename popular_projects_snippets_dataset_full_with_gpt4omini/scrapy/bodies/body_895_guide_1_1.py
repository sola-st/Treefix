from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

class MockProtocol(Protocol):# pragma: no cover
    def requestTunnel(self):# pragma: no cover
        print('Tunnel requested')# pragma: no cover
    def connectFailed(self, failure):# pragma: no cover
        print('Connection failed') # pragma: no cover
protocolFactory = ClientFactory() # pragma: no cover
protocolFactory.protocol = MockProtocol # pragma: no cover
self = type('Mock', (object,), {'_protocolFactory': None, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
def mock_connect(protocolFactory):# pragma: no cover
    deferred = Deferred()# pragma: no cover
    deferred.callback(None)  # Simulate successful connection# pragma: no cover
    return deferred # pragma: no cover
super = type('MockSuper', (object,), {'connect': mock_connect})() # pragma: no cover

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
