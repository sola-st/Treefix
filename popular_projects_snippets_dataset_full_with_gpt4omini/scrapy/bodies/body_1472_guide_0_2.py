from typing import AsyncIterator # pragma: no cover
from scrapy.http import Response as ScrapyResponse # pragma: no cover

class MockSpider(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockResponse:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
response = MockResponse()# pragma: no cover
spider = MockSpider()# pragma: no cover
# pragma: no cover
async def async_generator():# pragma: no cover
    yield {'key': 'value'}# pragma: no cover
# pragma: no cover
result = async_generator()  # Assigning the async generator to result# pragma: no cover
# pragma: no cover
self = type('Mock', (), {'_init_depth': lambda self, r, s: None, '_filter': lambda self, r, res, spi: True})() # pragma: no cover

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
