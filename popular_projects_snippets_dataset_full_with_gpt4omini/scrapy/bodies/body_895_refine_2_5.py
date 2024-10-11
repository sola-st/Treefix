from twisted.internet.defer import Deferred # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
protocolFactory = object() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda x: x # pragma: no cover
self.connectFailed = lambda err: print('Connection failed:', err) # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import protocol # pragma: no cover

class MockProtocol(protocol.Protocol): pass # pragma: no cover
class MockFactory(protocol.Factory): # pragma: no cover
    def buildProtocol(self, addr): return MockProtocol() # pragma: no cover
self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: x, 'connectFailed': lambda x: print('Failed:', x), '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
protocolFactory = MockFactory() # pragma: no cover

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
