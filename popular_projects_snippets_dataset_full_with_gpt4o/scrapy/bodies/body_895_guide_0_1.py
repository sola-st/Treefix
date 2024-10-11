from twisted.internet.defer import Deferred # pragma: no cover
import sys # pragma: no cover

class MockBaseClass: # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class MockSuper(MockBaseClass): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = type('Mock', (MockSuper,), {})() # pragma: no cover
self._protocolFactory = object() # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
 # pragma: no cover
def requestTunnel(result): # pragma: no cover
    print('requestTunnel called') # pragma: no cover
 # pragma: no cover
def connectFailed(failure): # pragma: no cover
    print('connectFailed called') # pragma: no cover
 # pragma: no cover
self.requestTunnel = requestTunnel # pragma: no cover
self.connectFailed = connectFailed # pragma: no cover
sys.exit = lambda x: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
self._protocolFactory = protocolFactory
_l_(21052)
connectDeferred = super().connect(protocolFactory)
_l_(21053)
connectDeferred.addCallback(self.requestTunnel)
_l_(21054)
connectDeferred.addErrback(self.connectFailed)
_l_(21055)
aux = self._tunnelReadyDeferred
_l_(21056)
exit(aux)
