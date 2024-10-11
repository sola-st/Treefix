from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import CertificateOptions # pragma: no cover
from twisted.web.client import BrowserLikePolicyForHTTPS # pragma: no cover
from zope.interface import implementer # pragma: no cover

def to_unicode(value): # pragma: no cover
    if isinstance(value, bytes): # pragma: no cover
        return value.decode('utf-8') # pragma: no cover
    return str(value) # pragma: no cover
class MockFactory: # pragma: no cover
    host = b'localhost' # pragma: no cover
    port = 80 # pragma: no cover
    scheme = b'http' # pragma: no cover
factory = MockFactory() # pragma: no cover
def create_instance(objcls, settings, crawler): # pragma: no cover
    return objcls() # pragma: no cover
class MockSelf: # pragma: no cover
    ClientContextFactory = BrowserLikePolicyForHTTPS # pragma: no cover
    _settings = {} # pragma: no cover
    _crawler = None # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http10.py
from l3.Runtime import _l_
try:
    from twisted.internet import reactor
    _l_(16526)

except ImportError:
    pass
host, port = to_unicode(factory.host), factory.port
_l_(16527)
if factory.scheme == b'https':
    _l_(16530)

    client_context_factory = create_instance(
        objcls=self.ClientContextFactory,
        settings=self._settings,
        crawler=self._crawler,
    )
    _l_(16528)
    aux = reactor.connectSSL(host, port, factory, client_context_factory)
    _l_(16529)
    exit(aux)
aux = reactor.connectTCP(host, port, factory)
_l_(16531)
exit(aux)
