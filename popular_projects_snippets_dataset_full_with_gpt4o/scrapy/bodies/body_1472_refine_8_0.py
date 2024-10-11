from unittest.mock import AsyncMock, Mock # pragma: no cover

response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = [Mock()] # pragma: no cover
self = type('MockSelf', (object,), {'_init_depth': Mock(), '_filter': AsyncMock(return_value=True)})() # pragma: no cover

import types # pragma: no cover
import collections.abc # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover
class AsyncIter(collections.abc.AsyncIterable):# pragma: no cover
    def __init__(self, items):# pragma: no cover
        self.items = items# pragma: no cover
    async def __aiter__(self):# pragma: no cover
        for item in self.items:# pragma: no cover
            yield item# pragma: no cover
result = AsyncIter([1, 2, 3]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
from l3.Runtime import _l_
self._init_depth(response, spider)
_l_(19836)
async for r in result or ():
    _l_(19839)

    if self._filter(r, response, spider):
        _l_(19838)

        aux = r
        _l_(19837)
        exit(aux)
