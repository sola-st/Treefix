from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class Mock(Protocol):# pragma: no cover
    def requestTunnel(self): pass# pragma: no cover
    def connectFailed(self, error): pass# pragma: no cover
# pragma: no cover
self = type('MockSelf', (object,), {'_protocolFactory': None, '_tunnelReadyDeferred': Deferred(), 'requestTunnel': Mock.requestTunnel, 'connectFailed': Mock.connectFailed})() # pragma: no cover
protocolFactory = type('MockFactory', (object,), {})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class BaseProtocol(Protocol):# pragma: no cover
    def connect(self, factory):# pragma: no cover
        return Deferred()# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._protocolFactory = None# pragma: no cover
        self._tunnelReadyDeferred = Deferred()# pragma: no cover
        self.requestTunnel = lambda: None# pragma: no cover
        self.connectFailed = lambda err: print('Connection failed:', err)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
protocolFactory = BaseProtocol() # pragma: no cover

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
