import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockResponse: pass # pragma: no cover
class MyClass: # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        pass # pragma: no cover
    async def result_gen(self): # pragma: no cover
        yield 'mock_result' # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
self = MyClass() # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
result = self.result_gen() # pragma: no cover

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
