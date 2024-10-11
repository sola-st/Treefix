from twisted.internet import reactor # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS # pragma: no cover
from twisted.internet.defer import DeferredSemaphore # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = BrowserLikePolicyForHTTPS() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = DeferredSemaphore(tokens=5) # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS # pragma: no cover
from twisted.internet.defer import DeferredSemaphore # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = BrowserLikePolicyForHTTPS() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = DeferredSemaphore(tokens=5) # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover
self = type('Mock', (Protocol,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
