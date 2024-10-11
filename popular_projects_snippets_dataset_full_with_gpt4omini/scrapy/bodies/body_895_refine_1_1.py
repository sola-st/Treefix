from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
protocolFactory = Mock() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda: None # pragma: no cover
self.connectFailed = lambda error: None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockProtocol(Protocol): # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        return Deferred() # pragma: no cover
 # pragma: no cover
class Mock:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self._protocolFactory = None # pragma: no cover
        self.requestTunnel = lambda: None # pragma: no cover
        self.connectFailed = lambda error: None # pragma: no cover
        self._tunnelReadyDeferred = Deferred() # pragma: no cover
        self.protocol_instance = MockProtocol() # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
protocolFactory = self.protocol_instance # pragma: no cover

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
