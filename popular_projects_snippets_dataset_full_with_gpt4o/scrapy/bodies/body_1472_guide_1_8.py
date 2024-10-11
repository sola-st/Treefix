import asyncio # pragma: no cover
import sys # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockResponse: pass # pragma: no cover
class SelfType: # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        pass # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
self = SelfType() # pragma: no cover
async def mock_result_gen(): # pragma: no cover
    yield 1 # pragma: no cover
result = mock_result_gen() # pragma: no cover
async def run(): # pragma: no cover
    self._init_depth(response, spider) # pragma: no cover
    async for r in result or (): # pragma: no cover
        if self._filter(r, response, spider): # pragma: no cover
            aux = r # pragma: no cover
asyncio.run(run()) # pragma: no cover

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
