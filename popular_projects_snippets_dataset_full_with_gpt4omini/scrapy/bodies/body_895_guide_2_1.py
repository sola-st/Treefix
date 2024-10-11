from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class MockProtocolFactory: pass # pragma: no cover
protocolFactory = MockProtocolFactory() # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
def mock_connect(factory): # pragma: no cover
    deferred = Deferred() # pragma: no cover
    reactor.callLater(0, deferred.callback, None)  # Simulate successful connection # pragma: no cover
    return deferred # pragma: no cover
super = type('MockSuper', (object,), {'connect': mock_connect})() # pragma: no cover
self.requestTunnel = lambda result: print('Tunnel established') # pragma: no cover
self.connectFailed = lambda failure: print('Connection failed:', failure) # pragma: no cover

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
