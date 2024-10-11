from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from types import SimpleNamespace # pragma: no cover

protocolFactory = Protocol() # pragma: no cover
self = SimpleNamespace(_protocolFactory=None, requestTunnel=lambda x: x, connectFailed=lambda x: x, _tunnelReadyDeferred=Deferred()) # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol, ClientFactory # pragma: no cover

class MyClientFactory(ClientFactory): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._protocolFactory = Protocol # pragma: no cover
        self._tunnelReadyDeferred = Deferred() # pragma: no cover
 # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.addCallback(self.requestTunnel) # pragma: no cover
        d.addErrback(self.connectFailed) # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
    def requestTunnel(self, result): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def connectFailed(self, failure): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = MyClientFactory() # pragma: no cover
protocolFactory = Protocol() # pragma: no cover

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
