import asyncio # pragma: no cover
from scrapy.http.response import Response # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
self = type('MockSelf', (object,), {'_process_spider_exception': lambda self, response, spider, failure, index: []})() # pragma: no cover
response = Response(url='http://example.com') # pragma: no cover
spider = Spider(name='example_spider') # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

import asyncio # pragma: no cover
from scrapy.http.response import Response # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class AsyncIterableWrapper: # pragma: no cover
    def __init__(self, iterable): # pragma: no cover
        self._iterable = iterable # pragma: no cover
    def __aiter__(self): # pragma: no cover
        self._iterator = iter(self._iterable) # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        try: # pragma: no cover
            value = next(self._iterator) # pragma: no cover
        except StopIteration: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
        await asyncio.sleep(0)  # yield control to the event loop # pragma: no cover
        return value # pragma: no cover
 # pragma: no cover
iterable = AsyncIterableWrapper([1, 2, 3]) # pragma: no cover
self = type('MockSelf', (object,), {'_process_spider_exception': lambda self, response, spider, failure, index: []})() # pragma: no cover
response = Response(url='http://example.com') # pragma: no cover
spider = Spider(name='example_spider') # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
try:
    _l_(20076)

    async for r in iterable:
        _l_(20070)

        aux = r
        _l_(20069)
        exit(aux)
except Exception as ex:
    _l_(20075)

    exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                      exception_processor_index)
    _l_(20071)
    if isinstance(exception_result, Failure):
        _l_(20073)

        raise
        _l_(20072)
    recover_to.extend(exception_result)
    _l_(20074)
