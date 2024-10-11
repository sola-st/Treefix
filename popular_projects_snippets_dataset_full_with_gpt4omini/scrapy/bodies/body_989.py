# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
assert self.spider is not None  # typing

if not isinstance(result, (Request, Response, Failure)):
    raise TypeError(f"Incorrect type: expected Request, Response or Failure, got {type(result)}: {result!r}")

# downloader middleware can return requests (for example, redirects)
if isinstance(result, Request):
    self.crawl(result)
    exit(None)

d = self.scraper.enqueue_scrape(result, request, self.spider)
d.addErrback(
    lambda f: logger.error(
        "Error while enqueuing downloader output",
        exc_info=failure_to_exc_info(f),
        extra={'spider': self.spider},
    )
)
exit(d)
