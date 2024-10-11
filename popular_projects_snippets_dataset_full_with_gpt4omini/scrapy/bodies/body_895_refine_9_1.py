from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: x, 'connectFailed': lambda x: x, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
protocolFactory = type('MockFactory', (object,), {})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol):# pragma: no cover
    def __init__(self, factory):# pragma: no cover
        self.factory = factory# pragma: no cover
    def requestTunnel(self):# pragma: no cover
        pass# pragma: no cover
    def connectFailed(self, error):# pragma: no cover
        print('Connection failed:', error) # pragma: no cover
self = MockProtocol(None) # pragma: no cover
protocolFactory = None # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover

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
