import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class MockSpider: # pragma: no cover
    def _process_spider_exception(self, response, spider, failure, exception_processor_index): # pragma: no cover
        return [] # pragma: no cover
 # pragma: no cover
async def async_iterable(): # pragma: no cover
    for i in range(3): # pragma: no cover
        yield i # pragma: no cover
 # pragma: no cover
    if aux == 2:  # Check specific value to trigger exception # pragma: no cover
        raise Exception('Simulated exception for testing') # pragma: no cover
 # pragma: no cover
iterable = async_iterable() # pragma: no cover
self = MockSpider() # pragma: no cover
response = None # pragma: no cover
spider = None # pragma: no cover
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
