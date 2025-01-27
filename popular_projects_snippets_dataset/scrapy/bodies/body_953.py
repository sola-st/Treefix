# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
self.settings = crawler.settings
self.signals = crawler.signals
self.slots = {}
self.active = set()
self.handlers = DownloadHandlers(crawler)
self.total_concurrency = self.settings.getint('CONCURRENT_REQUESTS')
self.domain_concurrency = self.settings.getint('CONCURRENT_REQUESTS_PER_DOMAIN')
self.ip_concurrency = self.settings.getint('CONCURRENT_REQUESTS_PER_IP')
self.randomize_delay = self.settings.getbool('RANDOMIZE_DOWNLOAD_DELAY')
self.middleware = DownloaderMiddlewareManager.from_crawler(crawler)
self._slot_gc_loop = task.LoopingCall(self._slot_gc)
self._slot_gc_loop.start(60)
