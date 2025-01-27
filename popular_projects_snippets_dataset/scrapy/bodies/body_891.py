# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
proxyHost, proxyPort, self._proxyAuthHeader = proxyConf
super().__init__(reactor, proxyHost, proxyPort, timeout, bindAddress)
self._tunnelReadyDeferred = defer.Deferred()
self._tunneledHost = host
self._tunneledPort = port
self._contextFactory = contextFactory
self._connectBuffer = bytearray()
