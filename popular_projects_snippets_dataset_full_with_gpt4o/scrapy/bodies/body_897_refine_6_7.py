from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = object()  # Twisted's reactor object # pragma: no cover
contextFactory = object()  # Some context factory object, typically an SSL context # pragma: no cover
connectTimeout = 30  # Timeout in seconds for connections # pragma: no cover
bindAddress = 'localhost'  # Local address to bind connections to # pragma: no cover
pool = []  # Example: an empty list to represent a pool of connections or objects # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080}  # Example proxy configuration # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': proxyConf, '_contextFactory': contextFactory})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
proxyConf = {'host': 'proxy.example.com', 'port': 8080} # pragma: no cover
superclass = type('Superclass', (object,), {'__init__': lambda self, reactor, contextFactory, connectTimeout, bindAddress, pool: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
