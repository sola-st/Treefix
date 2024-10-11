from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet import reactor # pragma: no cover

def to_unicode(value): return value.decode('utf-8') # pragma: no cover
class MockFactory: host = 'localhost'; port = 8080; scheme = b'https' # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

def to_unicode(value): return value if isinstance(value, str) else value.decode('utf-8') # pragma: no cover
class MockFactory: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.host = 'localhost' # pragma: no cover
        self.port = 4443 # pragma: no cover
        self.scheme = b'https' # pragma: no cover
# pragma: no cover
factory = MockFactory() # pragma: no cover
def create_instance(objcls, settings, crawler): return objcls() # pragma: no cover
class MockClientContextFactory(ClientContextFactory): pass # pragma: no cover
self = type('MockSelf', (object,), {'ClientContextFactory': MockClientContextFactory, '_settings': {}, '_crawler': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http10.py
from l3.Runtime import _l_
try:
    from twisted.internet import reactor
    _l_(5456)

except ImportError:
    pass
host, port = to_unicode(factory.host), factory.port
_l_(5457)
if factory.scheme == b'https':
    _l_(5460)

    client_context_factory = create_instance(
        objcls=self.ClientContextFactory,
        settings=self._settings,
        crawler=self._crawler,
    )
    _l_(5458)
    aux = reactor.connectSSL(host, port, factory, client_context_factory)
    _l_(5459)
    exit(aux)
aux = reactor.connectTCP(host, port, factory)
_l_(5461)
exit(aux)
