from typing import AsyncIterable, List # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
Failure = Mock() # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover
self._process_spider_exception = Mock(return_value=[Failure()]) # pragma: no cover

from typing import AsyncIterable, List # pragma: no cover
import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

async def mock_async_iterable(): # pragma: no cover
    for i in [1, 2, 3]: # pragma: no cover
        yield i # pragma: no cover
iterable = mock_async_iterable() # pragma: no cover
self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover

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
