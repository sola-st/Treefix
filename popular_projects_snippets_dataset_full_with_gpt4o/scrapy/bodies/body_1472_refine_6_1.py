import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = 'MockResponse' # pragma: no cover
spider = 'MockSpider' # pragma: no cover
result = [1, 2, 3] # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = 'MockResponse' # pragma: no cover
spider = 'MockSpider' # pragma: no cover
class AsyncIterator:# pragma: no cover
    def __init__(self, iterable):# pragma: no cover
        self.iterable = iterable# pragma: no cover
        self.iter = iter(iterable)# pragma: no cover
# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
# pragma: no cover
    async def __anext__(self):# pragma: no cover
        try:# pragma: no cover
            return next(self.iter)# pragma: no cover
        except StopIteration:# pragma: no cover
            raise StopAsyncIteration# pragma: no cover
result = AsyncIterator([1, 2, 3]) # pragma: no cover

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
