from types import SimpleNamespace # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = SimpleNamespace() # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
result = [SimpleNamespace()] # pragma: no cover

import types # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover
class AsyncIteratorWrapper:# pragma: no cover
    def __init__(self, wrapped):# pragma: no cover
        self._wrapped = wrapped# pragma: no cover
    # pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    # pragma: no cover
    async def __anext__(self):# pragma: no cover
        try:# pragma: no cover
            return self._wrapped.pop(0)# pragma: no cover
        except IndexError:# pragma: no cover
            raise StopAsyncIteration# pragma: no cover
result = AsyncIteratorWrapper([1, 2, 3]) # pragma: no cover

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
