from twisted.internet.defer import Deferred # pragma: no cover

protocolFactory = type('MockProtocolFactory', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_protocolFactory': None, # pragma: no cover
    'requestTunnel': lambda x: None, # pragma: no cover
    'connectFailed': lambda x: None, # pragma: no cover
    '_tunnelReadyDeferred': Deferred() # pragma: no cover
})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

class BaseClientFactory(ClientFactory): # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
protocolFactory = ClientFactory() # pragma: no cover
self = type('MockSelf', (BaseClientFactory,), { # pragma: no cover
   '_protocolFactory': protocolFactory, # pragma: no cover
   'requestTunnel': lambda x: None, # pragma: no cover
   'connectFailed': lambda x: None, # pragma: no cover
   '_tunnelReadyDeferred': Deferred() # pragma: no cover
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
