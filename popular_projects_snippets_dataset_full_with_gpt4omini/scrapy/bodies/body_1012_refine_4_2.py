from typing import AsyncIterable, List # pragma: no cover

class Mock: pass; self = type('Mock', (object,), {'_process_spider_exception': lambda self, response, spider, failure, index: [failure]})() # pragma: no cover
response = {'status': 200, 'data': 'some response data'} # pragma: no cover
spider = 'example_spider' # pragma: no cover
exception_processor_index = 0 # pragma: no cover
recover_to = [] # pragma: no cover

from typing import AsyncIterable, List # pragma: no cover
import asyncio # pragma: no cover

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
