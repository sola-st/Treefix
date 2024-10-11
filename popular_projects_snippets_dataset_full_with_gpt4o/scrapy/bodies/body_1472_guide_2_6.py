import asyncio # pragma: no cover
import sys # pragma: no cover

class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockResponse: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        pass # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
async def mock_result_gen(): # pragma: no cover
    yield 1 # pragma: no cover
 # pragma: no cover
result = mock_result_gen() # pragma: no cover

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
