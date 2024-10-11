from twisted.internet.defer import Deferred # pragma: no cover
from twisted.protocols.basic import LineReceiver # pragma: no cover

protocolFactory = LineReceiver() # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    '_protocolFactory': protocolFactory,# pragma: no cover
    'requestTunnel': lambda *args, **kwargs: None,# pragma: no cover
    'connectFailed': lambda *args, **kwargs: None,# pragma: no cover
    '_tunnelReadyDeferred': Deferred()# pragma: no cover
})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.protocols.basic import LineReceiver # pragma: no cover

protocolFactory = LineReceiver() # pragma: no cover
class BaseClass:# pragma: no cover
    def connect(self, _):# pragma: no cover
        d = Deferred()# pragma: no cover
        d.callback(None)# pragma: no cover
        return d # pragma: no cover
self = type('Mock', (BaseClass,), {# pragma: no cover
    '_protocolFactory': protocolFactory,# pragma: no cover
    'requestTunnel': lambda *args, **kwargs: None,# pragma: no cover
    'connectFailed': lambda *args, **kwargs: None,# pragma: no cover
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
