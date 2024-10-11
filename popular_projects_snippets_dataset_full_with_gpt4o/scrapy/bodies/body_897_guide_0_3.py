from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS, HTTPConnectionPool # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover

proxyConf = {'hostname': 'proxy.example.com', 'port': 8080, 'username': 'user', 'password': 'pass'} # pragma: no cover
contextFactory = BrowserLikePolicyForHTTPS() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = HTTPConnectionPool(reactor) # pragma: no cover
class Mock(ClientFactory):# pragma: no cover
    def __init__(self):# pragma: no cover
        super(Mock, self).__init__()# pragma: no cover
Mock = type('Mock', (ClientFactory,), {})()# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
