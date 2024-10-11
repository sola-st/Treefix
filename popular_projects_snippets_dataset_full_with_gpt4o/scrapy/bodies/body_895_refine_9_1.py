from twisted.internet import defer # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
protocolFactory = type('MockFactory', (object,), {'buildProtocol': lambda self, addr: None})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda _: None # pragma: no cover
self.connectFailed = lambda _: None # pragma: no cover
self._tunnelReadyDeferred = defer.Deferred() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover
from twisted.internet import reactor # pragma: no cover

protocolFactory = ClientFactory() # pragma: no cover
self = type('MockBase', (object,), {})() # pragma: no cover
super_class = type('MockSuperClass', (object,), { # pragma: no cover
    'connect': lambda self, factory: Deferred() # pragma: no cover
}) # pragma: no cover

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
