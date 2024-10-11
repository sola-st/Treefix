from twisted.internet import reactor # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

to_unicode = lambda x: x.decode('utf-8') if isinstance(x, bytes) else x # pragma: no cover
factory = type('MockFactory', (object,), {'host': b'localhost', 'port': 8080, 'scheme': b'http'})() # pragma: no cover
create_instance = lambda objcls, settings, crawler: objcls() # pragma: no cover
self = type('MockSelf', (object,), {'ClientContextFactory': ClientContextFactory, '_settings': {}, '_crawler': {}})() # pragma: no cover

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
