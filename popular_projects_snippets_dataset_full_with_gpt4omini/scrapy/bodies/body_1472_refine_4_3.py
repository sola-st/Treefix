from typing import List, Optional, AsyncIterator # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example response body'} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover
result = [{'data': 'result1'}, {'data': 'result2'}, {'data': 'result3'}] # pragma: no cover

from typing import AsyncIterator, Dict, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example response body'} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover
async def mock_result() -> AsyncIterator[Dict[str, Any]]:# pragma: no cover
    yield {'data': 'result1'}# pragma: no cover
    yield {'data': 'result2'}# pragma: no cover
    yield {'data': 'result3'}# pragma: no cover
 # pragma: no cover
result = mock_result() # pragma: no cover

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
