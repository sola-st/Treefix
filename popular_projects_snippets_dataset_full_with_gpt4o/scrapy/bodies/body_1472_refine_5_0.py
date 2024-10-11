import types # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover
result = [1, 2, 3] # pragma: no cover

import types # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover
class AsyncIterable:# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    # pragma: no cover
    async def __anext__(self):# pragma: no cover
        if not hasattr(self, 'items'):# pragma: no cover
            self.items = iter([1, 2, 3])# pragma: no cover
        try:# pragma: no cover
            return next(self.items)# pragma: no cover
        except StopIteration:# pragma: no cover
            raise StopAsyncIteration# pragma: no cover
result = AsyncIterable() # pragma: no cover

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
