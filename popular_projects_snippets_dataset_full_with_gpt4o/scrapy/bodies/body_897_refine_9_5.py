from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
proxyConf = {'proxyType': 'http', 'host': 'localhost', 'port': 8080} # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

reactor = reactor # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
proxyConf = {'proxyType': 'http', 'host': 'localhost', 'port': 8080} # pragma: no cover
self = type('Mock', (Protocol,), {'__init__': lambda self, reactor, contextFactory, connectTimeout, bindAddress, pool: None, '_proxyConf': proxyConf, '_contextFactory': contextFactory})(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
