from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
import datetime # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = datetime.timedelta(seconds=30) # pragma: no cover
bindAddress = ('localhost', 8000) # pragma: no cover
pool = None # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
proxyConf = {'proxy_type': 'http', 'proxy_host': 'proxy.local', 'proxy_port': 8080} # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.web.client import Agent # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

class BaseClass(object): pass # pragma: no cover
self = type('Mock', (BaseClass,), {})() # pragma: no cover
reactor = object() # pragma: no cover
contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = ('0.0.0.0', 8080) # pragma: no cover
pool = object() # pragma: no cover
proxyConf = {'host': 'proxy.local', 'port': 8080, 'enabled': True} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
