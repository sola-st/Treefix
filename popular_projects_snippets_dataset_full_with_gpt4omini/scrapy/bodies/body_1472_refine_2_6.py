from typing import AsyncIterator, Any # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example body', 'headers': {'Content-Type': 'text/html'}} # pragma: no cover
spider = MockSpider() # pragma: no cover

from typing import AsyncIterable, Any # pragma: no cover
import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
async def result_generator() -> AsyncIterable[dict]:# pragma: no cover
    for i in range(3):# pragma: no cover
        yield {'data': f'result{i + 1}'}# pragma: no cover
# pragma: no cover
result = result_generator() # pragma: no cover

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
