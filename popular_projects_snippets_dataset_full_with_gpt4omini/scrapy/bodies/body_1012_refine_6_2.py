from typing import AsyncIterable # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=object) # pragma: no cover
response = {'status': 200, 'data': 'OK'} # pragma: no cover
spider = 'test_spider' # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover
self._process_spider_exception = Mock(return_value=['recovered']) # pragma: no cover

import asyncio # pragma: no cover

async def async_iterable(): return (x for x in range(3)) # pragma: no cover
iterable = async_iterable() # pragma: no cover
class Mock: # pragma: no cover
    def _process_spider_exception(self, response, spider, failure, index): # pragma: no cover
        return [failure] # pragma: no cover
self = Mock() # pragma: no cover
response = {'status': 200, 'data': 'mock data'} # pragma: no cover
spider = 'mock_spider' # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
try:
    _l_(8729)

    async for r in iterable:
        _l_(8723)

        aux = r
        _l_(8722)
        exit(aux)
except Exception as ex:
    _l_(8728)

    exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                      exception_processor_index)
    _l_(8724)
    if isinstance(exception_result, Failure):
        _l_(8726)

        raise
        _l_(8725)
    recover_to.extend(exception_result)
    _l_(8727)
