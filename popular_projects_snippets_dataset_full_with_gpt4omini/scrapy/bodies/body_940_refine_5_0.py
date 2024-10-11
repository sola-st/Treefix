from twisted.protocols.basic import LineReceiver # pragma: no cover
from twisted.internet import defer, reactor # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockProtocol:# pragma: no cover
    def timeout(self):# pragma: no cover
        print('Timeout triggered') # pragma: no cover
class MockClientFactory(ClientFactory):# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return MockProtocol() # pragma: no cover
ClientFactory = MockClientFactory() # pragma: no cover
self = type('Mock', (object,), {'followRedirect': True, 'afterFoundGet': lambda: None, 'timeout': 5, 'deferred': Deferred(), '_cancelTimeout': lambda self, call: None})() # pragma: no cover
addr = ('127.0.0.1', 8080) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
from l3.Runtime import _l_
p = ClientFactory.buildProtocol(self, addr)
_l_(9883)
p.followRedirect = self.followRedirect
_l_(9884)
p.afterFoundGet = self.afterFoundGet
_l_(9885)
if self.timeout:
    _l_(9890)

    try:
        from twisted.internet import reactor
        _l_(9887)

    except ImportError:
        pass
    timeoutCall = reactor.callLater(self.timeout, p.timeout)
    _l_(9888)
    self.deferred.addBoth(self._cancelTimeout, timeoutCall)
    _l_(9889)
aux = p
_l_(9891)
exit(aux)
