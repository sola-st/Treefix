# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
if callback:
    cb_res = callback(response, **cb_kwargs) or ()
    if isinstance(cb_res, AsyncIterable):
        cb_res = await collect_asyncgen(cb_res)
    elif isinstance(cb_res, Awaitable):
        cb_res = await cb_res
    cb_res = self.process_results(response, cb_res)
    for request_or_item in iterate_spider_output(cb_res):
        exit(request_or_item)

if follow and self._follow_links:
    for request_or_item in self._requests_to_follow(response):
        exit(request_or_item)
