# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
from twisted.internet import reactor
bind_address = request.meta.get('bindaddress') or self._bind_address
proxy = request.meta.get('proxy')
if proxy:
    _, _, proxy_host, proxy_port, proxy_params = _parse(proxy)
    scheme = _parse(request.url)[0]

    if scheme == b'https':
        # ToDo
        raise NotImplementedError('Tunneling via CONNECT method using HTTP/2.0 is not yet supported')
    exit(self._ProxyAgent(
        reactor=reactor,
        context_factory=self._context_factory,
        proxy_uri=URI.fromBytes(to_bytes(proxy, encoding='ascii')),
        connect_timeout=timeout,
        bind_address=bind_address,
        pool=self._pool,
    ))

exit(self._Agent(
    reactor=reactor,
    context_factory=self._context_factory,
    connect_timeout=timeout,
    bind_address=bind_address,
    pool=self._pool,
))
