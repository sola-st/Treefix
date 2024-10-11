from twisted.internet import defer # pragma: no cover

class MockSuper:# pragma: no cover
    def connect(self, protocolFactory):# pragma: no cover
        d = defer.Deferred()# pragma: no cover
        return d # pragma: no cover
self = type('SelfMock', (object,), {})() # pragma: no cover
super = MockSuper # pragma: no cover
protocolFactory = type('ProtocolFactoryMock', (object,), {})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover
self._tunnelReadyDeferred = defer.Deferred() # pragma: no cover
def requestTunnel(self, result):# pragma: no cover
    print('requestTunnel called')# pragma: no cover
    self._tunnelReadyDeferred.callback('tunnel_ready') # pragma: no cover
self.requestTunnel = requestTunnel.__get__(self, type(self)) # pragma: no cover
def connectFailed(self, failure):# pragma: no cover
    print('connectFailed called') # pragma: no cover
self.connectFailed = connectFailed.__get__(self, type(self)) # pragma: no cover

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
