import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockResponse: pass # pragma: no cover
 # pragma: no cover
class SelfType: # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        pass # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
self = SelfType() # pragma: no cover
 # pragma: no cover
class AsyncIterator: # pragma: no cover
    def __init__(self, lst): # pragma: no cover
        self._iter = iter(lst) # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        try: return next(self._iter) # pragma: no cover
        except StopIteration: raise StopAsyncIteration # pragma: no cover
 # pragma: no cover
result = AsyncIterator([1]) # pragma: no cover
 # pragma: no cover
async def main(): # pragma: no cover
    self._init_depth(response, spider) # pragma: no cover
    async for r in result or (): # pragma: no cover
        if self._filter(r, response, spider): # pragma: no cover
            aux = r # pragma: no cover
 # pragma: no cover
asyncio.run(main()) # pragma: no cover

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
