from twisted.internet.defer import Deferred # pragma: no cover

class ProtocolFactoryMock: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def super_connect(protocolFactory): # pragma: no cover
    d = Deferred() # pragma: no cover
    d.callback(protocolFactory) # pragma: no cover
    return d # pragma: no cover
 # pragma: no cover
def requestTunnel(protocol): # pragma: no cover
    print('Tunnel requested') # pragma: no cover
 # pragma: no cover
def connectFailed(failure): # pragma: no cover
    print('Connection failed') # pragma: no cover
 # pragma: no cover
class Super: # pragma: no cover
    connect = staticmethod(super_connect) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_protocolFactory': ProtocolFactoryMock(), # pragma: no cover
    '_tunnelReadyDeferred': Deferred(), # pragma: no cover
    'requestTunnel': requestTunnel, # pragma: no cover
    'connectFailed': connectFailed # pragma: no cover
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
