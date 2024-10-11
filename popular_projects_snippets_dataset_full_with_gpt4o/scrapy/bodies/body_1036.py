# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""
        Handle the downloaded response or failure through the spider callback/errback
        """
if not isinstance(result, (Response, Failure)):
    raise TypeError(f"Incorrect type: expected Response or Failure, got {type(result)}: {result!r}")
dfd = self._scrape2(result, request, spider)  # returns spider's processed output
dfd.addErrback(self.handle_spider_error, request, result, spider)
dfd.addCallback(self.handle_spider_output, request, result, spider)
exit(dfd)
