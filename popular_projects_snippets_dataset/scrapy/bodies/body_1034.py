# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
if self.slot is None:
    raise RuntimeError("Scraper slot not assigned")
dfd = self.slot.add_response_request(result, request)

def finish_scraping(_):
    self.slot.finish_response(result, request)
    self._check_if_closing(spider)
    self._scrape_next(spider)
    exit(_)

dfd.addBoth(finish_scraping)
dfd.addErrback(
    lambda f: logger.error('Scraper bug processing %(request)s',
                           {'request': request},
                           exc_info=failure_to_exc_info(f),
                           extra={'spider': spider}))
self._scrape_next(spider)
exit(dfd)
