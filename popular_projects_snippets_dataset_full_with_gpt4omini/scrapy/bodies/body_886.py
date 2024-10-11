# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
self._crawler = crawler

from twisted.internet import reactor
self._pool = HTTPConnectionPool(reactor, persistent=True)
self._pool.maxPersistentPerHost = settings.getint('CONCURRENT_REQUESTS_PER_DOMAIN')
self._pool._factory.noisy = False

self._contextFactory = load_context_factory_from_settings(settings, crawler)
self._default_maxsize = settings.getint('DOWNLOAD_MAXSIZE')
self._default_warnsize = settings.getint('DOWNLOAD_WARNSIZE')
self._fail_on_dataloss = settings.getbool('DOWNLOAD_FAIL_ON_DATALOSS')
self._disconnect_timeout = 1
