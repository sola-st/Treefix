from typing import AsyncIterator, Callable, Any, List # pragma: no cover
class MockSpider: pass # pragma: no cover
class MockResponse: pass # pragma: no cover

self = type('Mock', (object,), { '_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True })() # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover

from typing import AsyncIterable, Dict, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'_init_depth': lambda response, spider: None, '_filter': lambda r, response, spider: True})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
async def mock_async_generator() -> AsyncIterable[Dict[str, Any]]:# pragma: no cover
    yield {'data': 'item1'}# pragma: no cover
    yield {'data': 'item2'}# pragma: no cover
    yield {'data': 'item3'}# pragma: no cover
result = mock_async_generator() # pragma: no cover

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
