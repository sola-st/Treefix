# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
async def process_callback_output(result: Union[Iterable, AsyncIterable]
                                  ) -> Union[MutableChain, MutableAsyncChain]:
    exit(await self._process_callback_output(response, spider, result))

def process_spider_exception(_failure: Failure) -> Union[Failure, MutableChain]:
    exit(self._process_spider_exception(response, spider, _failure))

dfd = mustbe_deferred(self._process_spider_input, scrape_func, response, request, spider)
dfd.addCallbacks(callback=deferred_f_from_coro_f(process_callback_output), errback=process_spider_exception)
exit(dfd)
