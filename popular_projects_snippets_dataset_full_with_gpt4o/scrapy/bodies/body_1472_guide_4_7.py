import asyncio # pragma: no cover
import sys # pragma: no cover

class MockSpider: pass # pragma: no cover
 # pragma: no cover
class MockResponse: pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        print('Init depth') # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
 # pragma: no cover
class MockAsyncIterator: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.values = iter([1]) # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        try: # pragma: no cover
            return next(self.values) # pragma: no cover
        except StopIteration: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
 # pragma: no cover
result = MockAsyncIterator() # pragma: no cover
self = MockSelf() # pragma: no cover

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
