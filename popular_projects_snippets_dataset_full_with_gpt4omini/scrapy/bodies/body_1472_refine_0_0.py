from typing import AsyncIterable, Any # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover

from typing import AsyncIterable, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover
async def mock_async_iter(): return iter([{'data': 'item1'}, {'data': 'item2'}, {'data': 'item3'}]) # pragma: no cover
result: AsyncIterable[Any] = mock_async_iter() # pragma: no cover
self._init_depth = lambda response, spider: None # pragma: no cover
self._filter = lambda r, response, spider: True # pragma: no cover

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
