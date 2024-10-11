import asyncio # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.http import Response # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
class MockSpider(Spider): pass # pragma: no cover
self = type("MockSelf", (object,), {"_process_spider_exception": lambda self, response, spider, failure, index: []})() # pragma: no cover
response = Response(url="http://example.com") # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

iterable = (i for i in [1, 2, 3]) # pragma: no cover
response = None # pragma: no cover
spider = None # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover
self = type('MockSelf', (object,), {"_process_spider_exception": lambda self, response, spider, failure, index: failure}) # pragma: no cover

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
