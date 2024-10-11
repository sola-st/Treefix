from twisted.internet.defer import Deferred # pragma: no cover

def mock_super_connect(protocolFactory): # pragma: no cover
    d = Deferred() # pragma: no cover
    d.callback(None) # pragma: no cover
    return d # pragma: no cover
type_mock_super = type('MockSuper', (object,), {'connect': mock_super_connect}) # pragma: no cover
protocolFactory = object() # pragma: no cover

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
