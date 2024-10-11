from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30  # Timeout in seconds # pragma: no cover
bindAddress = ('localhost', 0)  # Address to bind to # pragma: no cover
pool = []  # Connection pool, could be a list of connections # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080}  # Proxy configuration # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
