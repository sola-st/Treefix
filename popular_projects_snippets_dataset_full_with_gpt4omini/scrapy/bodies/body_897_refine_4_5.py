from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 8080) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
proxyConf = {'proxy_type': 'http', 'proxy_address': 'proxy.example.com', 'proxy_port': 8080} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

class BaseProtocol(Protocol): pass # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = ('localhost', 0) # pragma: no cover
pool = [] # pragma: no cover
self = type('Mock', (BaseProtocol,), {})() # pragma: no cover
proxyConf = {'http': 'http://proxy.example.com:8080'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
