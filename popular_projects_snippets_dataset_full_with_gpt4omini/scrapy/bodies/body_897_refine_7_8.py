from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = {} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

class MockBase(object): pass # pragma: no cover
reactor = None # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 0) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (MockBase,), {'_proxyConf': {}, '_contextFactory': contextFactory})() # pragma: no cover
proxyConf = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
