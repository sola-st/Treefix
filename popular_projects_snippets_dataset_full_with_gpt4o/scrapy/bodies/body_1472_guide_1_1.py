import asyncio # pragma: no cover
import sys # pragma: no cover

response = type('MockResponse', (object,), {})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
'_init_depth': lambda self, response, spider: None, # pragma: no cover
'_filter': lambda self, r, response, spider: True # pragma: no cover
})() # pragma: no cover
class MockAsyncIterable: # pragma: no cover
    def __aiter__(self): # pragma: no cover
        self.iter_values = iter([1, 2, 3]) # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        try: # pragma: no cover
            return next(self.iter_values) # pragma: no cover
        except StopIteration: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
result = MockAsyncIterable() # pragma: no cover

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
