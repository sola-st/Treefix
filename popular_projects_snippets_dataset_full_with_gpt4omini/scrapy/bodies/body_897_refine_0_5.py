from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('127.0.0.1', 0) # pragma: no cover
pool = object() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
proxyConf = {'http': 'http://proxy:port', 'https': 'https://proxy:port'} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover

class MockBase(Protocol): pass # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('127.0.0.1', 0) # pragma: no cover
pool = object() # pragma: no cover
self = type('Mock', (MockBase,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = {'http': 'http://proxy:port', 'https': 'https://proxy:port'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
