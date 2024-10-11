from typing import Any, AsyncGenerator # pragma: no cover

class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockResponse: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MyClass: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def _init_depth(self, response: Any, spider: Any): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def _filter(self, r: Any, response: Any, spider: Any) -> bool: # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
    async def result_gen(self) -> AsyncGenerator[Any, None]: # pragma: no cover
        yield 'mock_result' # pragma: no cover
 # pragma: no cover
mock_spider = MockSpider() # pragma: no cover
mock_response = MockResponse() # pragma: no cover
result = MyClass().result_gen() # pragma: no cover
instance = MyClass() # pragma: no cover
response = mock_response # pragma: no cover
spider = mock_spider # pragma: no cover

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
