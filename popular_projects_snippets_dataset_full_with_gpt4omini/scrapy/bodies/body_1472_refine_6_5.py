from typing import AsyncIterable, Dict, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=set) # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = Mock(name='spider') # pragma: no cover

from typing import AsyncIterable, Dict, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'_init_depth': lambda response, spider: None, '_filter': lambda r, response, spider: True})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example response body'} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
async def generate_results() -> AsyncIterable[Dict[str, Any]]:# pragma: no cover
    yield {'data': 'result1'}# pragma: no cover
    yield {'data': 'result2'}# pragma: no cover
    yield {'data': 'result3'}# pragma: no cover
result = generate_results() # pragma: no cover

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
