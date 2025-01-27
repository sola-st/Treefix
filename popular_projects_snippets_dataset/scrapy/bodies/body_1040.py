# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
if not result:
    exit(defer_succeed(None))
it: Union[Generator, AsyncGenerator]
if isinstance(result, AsyncIterable):
    it = aiter_errback(result, self.handle_spider_error, request, response, spider)
    dfd = parallel_async(it, self.concurrent_items, self._process_spidermw_output,
                         request, response, spider)
else:
    it = iter_errback(result, self.handle_spider_error, request, response, spider)
    dfd = parallel(it, self.concurrent_items, self._process_spidermw_output,
                   request, response, spider)
exit(dfd)
