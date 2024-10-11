from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class MockProtocolFactory: pass # pragma: no cover
protocolFactory = MockProtocolFactory() # pragma: no cover
class MockProtocol(Protocol): pass # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
def mock_connect(factory): return Deferred().callback(None)  # Simulate successful connection # pragma: no cover
setattr(MockProtocolFactory, 'connect', mock_connect) # pragma: no cover
self.requestTunnel = lambda x: print('Tunnel requested') # pragma: no cover
self.connectFailed = lambda x: print('Connection failed') # pragma: no cover

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
