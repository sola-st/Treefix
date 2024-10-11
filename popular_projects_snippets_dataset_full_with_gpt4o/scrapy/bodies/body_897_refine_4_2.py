from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 0) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = {} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 0) # pragma: no cover
pool = [] # pragma: no cover
proxyConf = {} # pragma: no cover
class MockBase(ClientFactory):  # Ensure proper initialization with super() # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool): # pragma: no cover
        super().__init__() # pragma: no cover
        self.reactor = reactor # pragma: no cover
        self.contextFactory = contextFactory # pragma: no cover
        self.connectTimeout = connectTimeout # pragma: no cover
        self.bindAddress = bindAddress # pragma: no cover
        self.pool = pool # pragma: no cover
class Mock(MockBase): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf): # pragma: no cover
        super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover
        self._proxyConf = proxyConf # pragma: no cover
        self._contextFactory = contextFactory # pragma: no cover
self = Mock(reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
