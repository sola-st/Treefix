from twisted.internet import reactor # pragma: no cover

class MockClientFactory(object):# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return MockProtocol() # pragma: no cover
class MockProtocol(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.followRedirect = True# pragma: no cover
        self.afterFoundGet = True# pragma: no cover
        self.timeout = lambda: print('Timeout called') # pragma: no cover
self = type('MockSelf', (object,), {'followRedirect': True, 'afterFoundGet': True, 'timeout': 5, 'deferred': type('MockDeferred', (object,), {'addBoth': lambda self, func1, func2: None})(), '_cancelTimeout': lambda self, call, timeout: print('Canceled Timeout')})() # pragma: no cover
addr = ('127.0.0.1', 8080) # pragma: no cover

from twisted.internet import reactor # pragma: no cover

class MockClientFactory:# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return MockProtocol() # pragma: no cover
class MockProtocol:# pragma: no cover
    def timeout(self):# pragma: no cover
        print('Timeout called') # pragma: no cover
ClientFactory = MockClientFactory() # pragma: no cover
class MockDeferred:# pragma: no cover
    def addBoth(self, func1, func2):# pragma: no cover
        return None # pragma: no cover
self = type('MockSelf', (), {'followRedirect': True, 'afterFoundGet': None, 'timeout': 5, 'deferred': MockDeferred(), '_cancelTimeout': lambda self, call: None})() # pragma: no cover
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
