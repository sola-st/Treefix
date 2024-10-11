from typing import AsyncIterable, Any # pragma: no cover
class MockSpider: pass # pragma: no cover
class MockResponse: pass # pragma: no cover

response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._init_depth = lambda r, s: None # pragma: no cover
self._filter = lambda r, res, spi: True # pragma: no cover

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
