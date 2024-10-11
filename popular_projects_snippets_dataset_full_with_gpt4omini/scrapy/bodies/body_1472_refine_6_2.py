from typing import AsyncIterable, Dict, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=set) # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = Mock(name='spider') # pragma: no cover

from typing import AsyncIterable, Dict, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider): pass# pragma: no cover
    def _filter(self, r, response, spider): return True # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
async def mock_async_iter():# pragma: no cover
    for item in [{'data': 'result1'}, {'data': 'result2'}, {'data': 'result3'}]:# pragma: no cover
        yield item # pragma: no cover
result = mock_async_iter() # pragma: no cover

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
