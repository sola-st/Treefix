# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
assert self.slot is not None  # typing
while self.slot.queue:
    response, request, deferred = self.slot.next_response_request_deferred()
    self._scrape(response, request, spider).chainDeferred(deferred)
