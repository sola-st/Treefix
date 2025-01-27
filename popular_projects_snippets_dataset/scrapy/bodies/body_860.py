# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
self._crawler = crawler

from twisted.internet import reactor
self._pool = H2ConnectionPool(reactor, settings)
self._context_factory = load_context_factory_from_settings(settings, crawler)
