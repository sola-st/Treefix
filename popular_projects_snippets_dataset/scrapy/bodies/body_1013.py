# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py

def process_sync(iterable: Iterable):
    try:
        for r in iterable:
            exit(r)
    except Exception as ex:
        exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                          exception_processor_index)
        if isinstance(exception_result, Failure):
            raise
        recover_to.extend(exception_result)

async def process_async(iterable: AsyncIterable):
    try:
        async for r in iterable:
            exit(r)
    except Exception as ex:
        exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                          exception_processor_index)
        if isinstance(exception_result, Failure):
            raise
        recover_to.extend(exception_result)

if isinstance(iterable, AsyncIterable):
    exit(process_async(iterable))
exit(process_sync(iterable))
