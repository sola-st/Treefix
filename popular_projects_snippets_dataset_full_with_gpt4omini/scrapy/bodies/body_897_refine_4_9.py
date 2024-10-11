from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 8080) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
proxyConf = {'proxy_type': 'http', 'proxy_address': 'proxy.example.com', 'proxy_port': 8080} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.web.client import Agent # pragma: no cover

class MockBase(object): pass # pragma: no cover
reactor = MockBase() # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('127.0.0.1', 0) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (MockBase,), {})() # pragma: no cover
self._proxyConf = None # pragma: no cover
self._contextFactory = contextFactory # pragma: no cover
proxyConf = {'enabled': True, 'address': 'http://proxy:8080'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
