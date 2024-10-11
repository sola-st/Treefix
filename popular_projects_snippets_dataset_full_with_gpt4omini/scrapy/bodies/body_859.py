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
