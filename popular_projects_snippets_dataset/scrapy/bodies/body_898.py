# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
exit(TunnelingTCP4ClientEndpoint(
    reactor=self._reactor,
    host=uri.host,
    port=uri.port,
    proxyConf=self._proxyConf,
    contextFactory=self._contextFactory,
    timeout=self._endpointFactory._connectTimeout,
    bindAddress=self._endpointFactory._bindAddress,
))
