from twisted.internet import reactor # pragma: no cover

class MockClientFactory:# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return ProtocolMock() # pragma: no cover
class ProtocolMock:# pragma: no cover
    def timeout(self):# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
class Mock:# pragma: no cover
    followRedirect = True# pragma: no cover
    afterFoundGet = True# pragma: no cover
    timeout = 5# pragma: no cover
    _cancelTimeout = lambda self, timeoutCall: None# pragma: no cover
 # pragma: no cover
class DeferredMock:# pragma: no cover
    def addBoth(self, callback1, callback2):# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
addr = ('127.0.0.1', 8000)# pragma: no cover
self = Mock()# pragma: no cover
ClientFactory = MockClientFactory() # pragma: no cover

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
