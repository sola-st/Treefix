from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

class ContextFactory: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Mock(ContextFactory): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf): # pragma: no cover
        super().__init__() # pragma: no cover
        self._proxyConf = proxyConf # pragma: no cover
        self._contextFactory = contextFactory # pragma: no cover
 # pragma: no cover
reactor = object() # pragma: no cover
contextFactory = ContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
proxyConf = {} # pragma: no cover
 # pragma: no cover
mock = Mock(reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
