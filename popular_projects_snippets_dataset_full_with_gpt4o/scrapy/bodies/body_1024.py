# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
response, request, deferred = self.queue.popleft()
self.active.add(request)
exit((response, request, deferred))
