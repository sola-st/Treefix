from twisted.internet import reactor # pragma: no cover

class MockClientFactory:# pragma: no cover
    @staticmethod# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return object()  # Mock Protocol object # pragma: no cover
class Mock:# pragma: no cover
    followRedirect = True# pragma: no cover
    afterFoundGet = lambda self: None# pragma: no cover
    timeout = 5# pragma: no cover
    deferred = object()  # Mock Deferred object# pragma: no cover
    def _cancelTimeout(self, result, timeoutCall):# pragma: no cover
        return result  # No-op method # pragma: no cover
self = Mock() # pragma: no cover
addr = ('127.0.0.1', 8080) # pragma: no cover

from twisted.internet import reactor # pragma: no cover

class MockClientFactory:# pragma: no cover
    @staticmethod# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return object()  # Mock Protocol object # pragma: no cover
class Mock:# pragma: no cover
    followRedirect = True# pragma: no cover
    afterFoundGet = lambda self: None# pragma: no cover
    timeout = 5# pragma: no cover
    deferred = object()  # Mock Deferred object# pragma: no cover
    def _cancelTimeout(self, result, timeoutCall):# pragma: no cover
        return result  # No-op method # pragma: no cover
ClientFactory = MockClientFactory() # pragma: no cover
self = Mock() # pragma: no cover
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
