# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
self.active.remove(request)
if isinstance(result, Response):
    self.active_size -= max(len(result.body), self.MIN_RESPONSE_SIZE)
else:
    self.active_size -= self.MIN_RESPONSE_SIZE
