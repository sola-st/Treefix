from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = object() # pragma: no cover
connectTimeout = 30  # seconds # pragma: no cover
bindAddress = None  # or ('localhost', 1337) for example # pragma: no cover
pool = []  # Empty list or proper connection pool object # pragma: no cover
proxyConf = {'proxyType': 'HTTP', 'host': 'localhost', 'port': 8080} # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': {}, '_contextFactory': None})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS # pragma: no cover
from twisted.internet.defer import DeferredSemaphore # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = BrowserLikePolicyForHTTPS() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = DeferredSemaphore(tokens=5) # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover
BaseClass = type('BaseClass', (object,), {'__init__': lambda self, reactor, contextFactory, connectTimeout, bindAddress, pool: None}) # pragma: no cover
self = type('Mock', (BaseClass,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
