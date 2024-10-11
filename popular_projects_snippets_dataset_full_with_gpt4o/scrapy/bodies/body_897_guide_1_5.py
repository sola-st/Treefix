from twisted.internet import reactor # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS # pragma: no cover

contextFactory = BrowserLikePolicyForHTTPS() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
proxyConf = {'proxy_host': 'localhost', 'proxy_port': 8080} # pragma: no cover
class MockSuper: # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool): # pragma: no cover
        pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
