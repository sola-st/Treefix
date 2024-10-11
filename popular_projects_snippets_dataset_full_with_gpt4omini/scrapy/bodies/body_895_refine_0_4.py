from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import reactor # pragma: no cover

self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: x, 'connectFailed': lambda x: x, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
protocolFactory = 'some_protocol_factory' # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol): pass # pragma: no cover
self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: x, 'connectFailed': lambda x: x, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
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
