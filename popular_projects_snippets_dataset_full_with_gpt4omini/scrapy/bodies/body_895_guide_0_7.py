from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

protocolFactory = type('MockProtocolFactory', (object,), {'buildProtocol': lambda self, addr: MockProtocol()})() # pragma: no cover
class MockProtocol(Protocol): pass # pragma: no cover
self = type('MockObject', (object,), {'_tunnelReadyDeferred': Deferred(), 'requestTunnel': lambda self, res: None, 'connectFailed': lambda self, err: None})() # pragma: no cover
super = type('MockSuper', (object,), {'connect': lambda self, protocolFactory: Deferred()})() # pragma: no cover

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
