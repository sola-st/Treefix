from twisted.internet.defer import Deferred # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
protocolFactory = object() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self.requestTunnel = lambda _: None # pragma: no cover
self.connectFailed = lambda _: None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
def connect(protocolFactory): # pragma: no cover
    d = Deferred() # pragma: no cover
    d.callback(None) # pragma: no cover
    return d # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol, ClientFactory # pragma: no cover

class MockBase(object): # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(None) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class MyClass(MockBase): # pragma: no cover
    def __init__(self, protocolFactory): # pragma: no cover
        self._protocolFactory = protocolFactory # pragma: no cover
        self.requestTunnel = lambda _: None # pragma: no cover
        self.connectFailed = lambda _: None # pragma: no cover
        self._tunnelReadyDeferred = Deferred() # pragma: no cover
 # pragma: no cover
protocolFactory = ClientFactory() # pragma: no cover
self = MyClass(protocolFactory) # pragma: no cover

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
