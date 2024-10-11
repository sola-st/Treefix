from twisted.internet.defer import Deferred # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._protocolFactory = None # pragma: no cover
self.requestTunnel = lambda x: None # pragma: no cover
self.connectFailed = lambda x: None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
protocolFactory = None # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol):# pragma: no cover
    def requestTunnel(self):# pragma: no cover
        pass# pragma: no cover
    def connectFailed(self, err):# pragma: no cover
        print('Connection failed:', err)# pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'_protocolFactory': None, 'requestTunnel': MockProtocol.requestTunnel, 'connectFailed': MockProtocol.connectFailed, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
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
