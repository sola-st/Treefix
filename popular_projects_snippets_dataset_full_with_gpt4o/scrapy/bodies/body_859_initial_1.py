from twisted.internet.protocol import ClientFactory # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
def to_unicode(value): return value.decode('utf-8') # pragma: no cover

factory = type('Mock', (ClientFactory,), {'host': b'localhost', 'port': 8080, 'scheme': b'https'})() # pragma: no cover
def create_instance(objcls, settings, crawler): return objcls() # pragma: no cover
self = type('Mock', (object,), {'ClientContextFactory': ClientContextFactory, '_settings': {}, '_crawler': None})() # pragma: no cover

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
