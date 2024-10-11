from twisted.internet.defer import Deferred # pragma: no cover

class MockSuper(object): # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        # Mimic an immediate callback for simplicity # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class MyClass(MockSuper): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._tunnelReadyDeferred = Deferred() # pragma: no cover
 # pragma: no cover
    def requestTunnel(self, _): # pragma: no cover
        print('Tunnel requested') # pragma: no cover
 # pragma: no cover
    def connectFailed(self, failure): # pragma: no cover
        print('Connection failed') # pragma: no cover
 # pragma: no cover
protocolFactory = object() # pragma: no cover
self = MyClass() # pragma: no cover

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
