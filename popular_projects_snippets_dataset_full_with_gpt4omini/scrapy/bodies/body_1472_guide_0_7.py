from typing import AsyncIterable, Any # pragma: no cover

class MockSpider: pass # pragma: no cover
spider = MockSpider() # pragma: no cover
result: AsyncIterable[Any] = [1, 2, 3] # pragma: no cover
def filter_mock(r, response, spider): return r % 2 == 0 # pragma: no cover
self = type('Mock', (), {'_init_depth': lambda self, response, spider: None, '_filter': filter_mock})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
from l3.Runtime import _l_
self._init_depth(response, spider)
_l_(8646)
async for r in result or ():
    _l_(8649)

    if self._filter(r, response, spider):
        _l_(8648)

        aux = r
        _l_(8647)
        exit(aux)
