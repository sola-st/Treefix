from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover

class MockContextFactory: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockReactor: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
proxyConf = {'host': 'localhost', 'port': 8080} # pragma: no cover
contextFactory = MockContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
 # pragma: no cover
class MockClientFactory(ClientFactory): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool): # pragma: no cover
        super().__init__() # pragma: no cover
        self._reactor = reactor # pragma: no cover
        self._contextFactory = contextFactory # pragma: no cover
        self._connectTimeout = connectTimeout # pragma: no cover
        self._bindAddress = bindAddress # pragma: no cover
        self._pool = pool # pragma: no cover
 # pragma: no cover
mock_client_factory = MockClientFactory(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
