from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

protocolFactory = ClientFactory() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda x: None # pragma: no cover
self.connectFailed = lambda x: None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol, ClientFactory # pragma: no cover

class BaseMock(ClientFactory): # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
protocolFactory = Protocol() # pragma: no cover
self = type('Mock', (BaseMock,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda x: None # pragma: no cover
self.connectFailed = lambda x: None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover

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
