reactor = type('Mock', (object,), {})() # pragma: no cover
contextFactory = type('Mock', (object,), {})() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = type('Mock', (object,), {})() # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = type('Mock', (object,), {})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import ReconnectingClientFactory # pragma: no cover

class CustomFactory(ReconnectingClientFactory):# pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool):# pragma: no cover
        super(CustomFactory, self).__init__()# pragma: no cover
        self._reactor = reactor# pragma: no cover
        self._contextFactory = contextFactory# pragma: no cover
        self._connectTimeout = connectTimeout# pragma: no cover
        self._bindAddress = bindAddress# pragma: no cover
        self._pool = pool # pragma: no cover
reactor = reactor # pragma: no cover
contextFactory = None # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = [] # pragma: no cover
self = CustomFactory(reactor, contextFactory, connectTimeout, bindAddress, pool) # pragma: no cover
proxyConf = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
