from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import CertificateOptions # pragma: no cover

class MockContextFactory(CertificateOptions):# pragma: no cover
    pass # pragma: no cover
contextFactory = MockContextFactory() # pragma: no cover
connectTimeout = 30 # pragma: no cover
bindAddress = None # pragma: no cover
pool = None # pragma: no cover
proxyConf = {'proxyHost': 'localhost', 'proxyPort': 8080} # pragma: no cover
class MockSuperClass:# pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool):# pragma: no cover
        pass # pragma: no cover
class MockClass(MockSuperClass): # pragma: no cover
    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf):# pragma: no cover
        super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)# pragma: no cover
        self._proxyConf = proxyConf# pragma: no cover
        self._contextFactory = contextFactory# pragma: no cover
mock_object = MockClass(reactor, contextFactory, connectTimeout, bindAddress, pool, proxyConf) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
_l_(17738)
self._proxyConf = proxyConf
_l_(17739)
self._contextFactory = contextFactory
_l_(17740)
