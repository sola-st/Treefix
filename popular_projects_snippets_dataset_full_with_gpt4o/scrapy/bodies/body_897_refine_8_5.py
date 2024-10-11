from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = ['http_proxy', 'https_proxy'] # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': {}, '_contextFactory': contextFactory})() # pragma: no cover
proxyConf = {'host': 'localhost', 'port': 8080} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = ['http_proxy', 'https_proxy'] # pragma: no cover
proxyConf = {'host': 'localhost', 'port': 8080} # pragma: no cover
BaseClass = type('BaseClass', (object,), {}) # pragma: no cover
self = type('MockClass', (BaseClass,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
