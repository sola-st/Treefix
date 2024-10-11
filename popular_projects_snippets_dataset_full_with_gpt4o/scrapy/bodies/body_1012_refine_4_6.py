import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
response = 'example_response' # pragma: no cover
spider = 'example_spider' # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

iterable = asyncio.Queue() # pragma: no cover
async def populate(queue):# pragma: no cover
    for i in range(3):# pragma: no cover
        await queue.put(i)# pragma: no cover
    await queue.put(None)# pragma: no cover
asyncio.run(populate(iterable)) # pragma: no cover
class MockSpider:# pragma: no cover
    def _process_spider_exception(self, response, spider, failure, index):# pragma: no cover
        return []# pragma: no cover
self = MockSpider() # pragma: no cover
response = 'example_response' # pragma: no cover
spider = 'example_spider' # pragma: no cover
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
