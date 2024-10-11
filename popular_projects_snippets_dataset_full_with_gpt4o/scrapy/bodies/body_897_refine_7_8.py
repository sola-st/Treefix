reactor = type('Mock', (object,), {})() # pragma: no cover
contextFactory = type('Mock', (object,), {})() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = type('Mock', (object,), {})() # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = type('Mock', (object,), {})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover
from twisted.internet.defer import DeferredSemaphore # pragma: no cover

class MockBase(object): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool): # pragma: no cover
        self.reactor = reactor # pragma: no cover
        self.contextFactory = contextFactory # pragma: no cover
        self.connectTimeout = connectTimeout # pragma: no cover
        self.bindAddress = bindAddress # pragma: no cover
        self.pool = pool # pragma: no cover
 # pragma: no cover
reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = ('localhost', 0) # pragma: no cover
pool = DeferredSemaphore(5) # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover
self = type('Mock', (MockBase,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
