from twisted.internet import defer # pragma: no cover

def to_unicode(input): return input.decode('utf-8') if isinstance(input, bytes) else input # pragma: no cover
factory = type('MockFactory', (object,), {'host': 'example.com', 'port': 443, 'scheme': b'https'})() # pragma: no cover
def create_instance(objcls, settings, crawler): return objcls(settings, crawler) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
'ClientContextFactory': object,  # pragma: no cover
'_settings': {}, # pragma: no cover
'_crawler': object # pragma: no cover
})() # pragma: no cover

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
