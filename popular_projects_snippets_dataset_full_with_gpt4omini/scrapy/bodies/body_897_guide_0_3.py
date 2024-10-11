from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

contextFactory = ClientContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
proxyConf = {'host': 'localhost', 'port': 8080} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(6739)
self._proxyConf = proxyConf
_l_(6740)
self._contextFactory = contextFactory
_l_(6741)
