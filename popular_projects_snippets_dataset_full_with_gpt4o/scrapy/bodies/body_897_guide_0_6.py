from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ReconnectingClientFactory # pragma: no cover

class MockContextFactory: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockReactor: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
proxyConf = {} # pragma: no cover
contextFactory = MockContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
 # pragma: no cover
class MockSuperClass(ReconnectingClientFactory, MockReactor): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool): # pragma: no cover
        ReconnectingClientFactory.__init__(self) # pragma: no cover
        self.reactor = reactor # pragma: no cover
        self.contextFactory = contextFactory # pragma: no cover
        self.connectTimeout = connectTimeout # pragma: no cover
        self.bindAddress = bindAddress # pragma: no cover
        self.pool = pool # pragma: no cover
 # pragma: no cover
super = type('MockSuperClass', (MockSuperClass,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
