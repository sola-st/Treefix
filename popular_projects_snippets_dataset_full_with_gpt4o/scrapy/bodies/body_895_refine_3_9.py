from twisted.internet.defer import Deferred # pragma: no cover

self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda x: None, 'connectFailed': lambda x: None, '_tunnelReadyDeferred': Deferred()})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover
from twisted.internet import reactor # pragma: no cover

protocolFactory = ClientFactory() # pragma: no cover
MockBase = type('MockBase', (object,), {# pragma: no cover
    'connect': lambda self, protocolFactory: Deferred()}) # pragma: no cover
self = type('Mock', (MockBase,), {# pragma: no cover
    '_protocolFactory': protocolFactory,# pragma: no cover
    'requestTunnel': lambda self, x: None,# pragma: no cover
    'connectFailed': lambda self, x: None,# pragma: no cover
    '_tunnelReadyDeferred': Deferred()# pragma: no cover
})() # pragma: no cover

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
