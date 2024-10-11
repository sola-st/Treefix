reactor = type('Mock', (object,), {})() # pragma: no cover
contextFactory = type('Mock', (object,), {})() # pragma: no cover
connectTimeout = 30.0 # pragma: no cover
bindAddress = ('localhost', 8080) # pragma: no cover
pool = type('Mock', (object,), {})() # pragma: no cover
self = type('Mock', (object,), {'_proxyConf': None, '_contextFactory': None})() # pragma: no cover
proxyConf = type('Mock', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
