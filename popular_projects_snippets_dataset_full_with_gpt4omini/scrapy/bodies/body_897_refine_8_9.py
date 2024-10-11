from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

connectTimeout = 10.0 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = None # pragma: no cover
proxyConf = {'host': 'proxy.server.com', 'port': 8081} # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
self._contextFactory = ClientContextFactory() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

class BaseClass: pass # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (BaseClass,), {'_proxyConf': {}, '_contextFactory': contextFactory})() # pragma: no cover
self._proxyConf = {'http': 'http://proxy.address:port'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
