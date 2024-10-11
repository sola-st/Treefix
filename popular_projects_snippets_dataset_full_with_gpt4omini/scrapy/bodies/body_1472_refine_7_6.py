from typing import AsyncIterator # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (), {'_init_depth': MagicMock(), '_filter': MagicMock(return_value=False)})() # pragma: no cover
response = 'mock_response' # pragma: no cover
spider = MockSpider() # pragma: no cover

from typing import AsyncIterable, Dict, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider): pass# pragma: no cover
    def _filter(self, r, response, spider): return True # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example response'} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
async def async_result():# pragma: no cover
    yield {'data': 'result1'}# pragma: no cover
    yield {'data': 'result2'}# pragma: no cover
    yield {'data': 'result3'} # pragma: no cover
result = async_result() # pragma: no cover

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
