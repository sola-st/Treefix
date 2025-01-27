# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
self.concurrency = concurrency
self.delay = delay
self.randomize_delay = randomize_delay

self.active = set()
self.queue = deque()
self.transferring = set()
self.lastseen = 0
self.latercall = None
