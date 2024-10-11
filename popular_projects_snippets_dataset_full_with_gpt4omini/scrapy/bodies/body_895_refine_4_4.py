from twisted.internet import defer # pragma: no cover

self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: None, 'connectFailed': lambda x: None, '_tunnelReadyDeferred': defer.Deferred()})() # pragma: no cover
protocolFactory = type('MockProtocolFactory', (object,), {})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol):# pragma: no cover
    def connectionMade(self):# pragma: no cover
        pass# pragma: no cover
    def requestTunnel(self):# pragma: no cover
        return 'Tunnel Requested'# pragma: no cover
    def connectFailed(self, error):# pragma: no cover
        print('Connection failed:', error)# pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'_protocolFactory': MockProtocol(), '_tunnelReadyDeferred': Deferred(), 'requestTunnel': MockProtocol.requestTunnel, 'connectFailed': MockProtocol.connectFailed})() # pragma: no cover
protocolFactory = MockProtocol() # pragma: no cover

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
