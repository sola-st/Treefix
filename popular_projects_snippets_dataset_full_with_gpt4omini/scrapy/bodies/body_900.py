# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
super().__init__(
    reactor=reactor,
    connectTimeout=connectTimeout,
    bindAddress=bindAddress,
    pool=pool,
)
self._proxyURI = URI.fromBytes(proxyURI)
