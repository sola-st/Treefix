# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from twisted.internet import reactor
bindaddress = request.meta.get('bindaddress') or self._bindAddress
proxy = request.meta.get('proxy')
if proxy:
    proxyScheme, proxyNetloc, proxyHost, proxyPort, proxyParams = _parse(proxy)
    scheme = _parse(request.url)[0]
    proxyHost = to_unicode(proxyHost)
    if scheme == b'https':
        proxyAuth = request.headers.get(b'Proxy-Authorization', None)
        proxyConf = (proxyHost, proxyPort, proxyAuth)
        exit(self._TunnelingAgent(
            reactor=reactor,
            proxyConf=proxyConf,
            contextFactory=self._contextFactory,
            connectTimeout=timeout,
            bindAddress=bindaddress,
            pool=self._pool,
        ))
    proxyScheme = proxyScheme or b'http'
    proxyURI = urlunparse((proxyScheme, proxyNetloc, proxyParams, '', '', ''))
    exit(self._ProxyAgent(
        reactor=reactor,
        proxyURI=to_bytes(proxyURI, encoding='ascii'),
        connectTimeout=timeout,
        bindAddress=bindaddress,
        pool=self._pool,
    ))

exit(self._Agent(
    reactor=reactor,
    contextFactory=self._contextFactory,
    connectTimeout=timeout,
    bindAddress=bindaddress,
    pool=self._pool,
))
