from twisted.internet.defer import Deferred # pragma: no cover
from types import MethodType # pragma: no cover

class ClientFactoryMock: # pragma: no cover
    @staticmethod # pragma: no cover
    def buildProtocol(self, addr): # pragma: no cover
        proto = type('ProtocolMock', (object,), {})() # pragma: no cover
        proto.timeout = lambda: None # pragma: no cover
        return proto # pragma: no cover
 # pragma: no cover
ClientFactory = ClientFactoryMock # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'followRedirect': True, # pragma: no cover
    'afterFoundGet': False, # pragma: no cover
    'timeout': 5, # pragma: no cover
    'deferred': Deferred(), # pragma: no cover
    '_cancelTimeout': lambda x, y: None # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
addr = '127.0.0.1' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
from l3.Runtime import _l_
p = ClientFactory.buildProtocol(self, addr)
_l_(21116)
p.followRedirect = self.followRedirect
_l_(21117)
p.afterFoundGet = self.afterFoundGet
_l_(21118)
if self.timeout:
    _l_(21123)

    try:
        from twisted.internet import reactor
        _l_(21120)

    except ImportError:
        pass
    timeoutCall = reactor.callLater(self.timeout, p.timeout)
    _l_(21121)
    self.deferred.addBoth(self._cancelTimeout, timeoutCall)
    _l_(21122)
aux = p
_l_(21124)
exit(aux)
