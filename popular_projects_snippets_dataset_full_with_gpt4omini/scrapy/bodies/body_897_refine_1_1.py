from twisted.internet import reactor # pragma: no cover
from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = None # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
proxyConf = {'proxyEnabled': True, 'proxyAddress': 'http://proxy.example.com:8080'} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

class MockBase: pass # pragma: no cover
self = type('MockSelf', (MockBase,), {})() # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 10 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = None # pragma: no cover
proxyConf = {'proxyEnabled': True, 'proxyAddress': 'http://proxy.example.com:8080'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
