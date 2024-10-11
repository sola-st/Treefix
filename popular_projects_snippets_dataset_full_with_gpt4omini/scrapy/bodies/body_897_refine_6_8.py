from twisted.internet import reactor # pragma: no cover
from twisted.web.http import Request # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = None # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._proxyConf = {} # pragma: no cover
self._contextFactory = contextFactory # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.web.client import Agent # pragma: no cover

class BaseClass: pass # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('127.0.0.1', 8080) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (BaseClass,), {})() # pragma: no cover
proxyConf = {'http': 'http://user:pass@proxyhost:port', 'https': 'https://user:pass@proxyhost:port'} # pragma: no cover
self._proxyConf = proxyConf # pragma: no cover
self._contextFactory = contextFactory # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
