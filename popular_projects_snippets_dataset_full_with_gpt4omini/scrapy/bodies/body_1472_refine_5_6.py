from typing import AsyncIterable, Callable, Dict, Any # pragma: no cover

class MockSpidey: pass # pragma: no cover
self = type('Mock', (object,), {'_init_depth': lambda response, spider: None, '_filter': lambda r, response, spider: False})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = MockSpidey() # pragma: no cover

from typing import AsyncIterable, Dict, Any # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True # pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover
# pragma: no cover
async def mock_iterable():# pragma: no cover
    for item in [{'data': 'item1'}, {'data': 'item2'}, {'data': 'item3'}]:# pragma: no cover
        yield item# pragma: no cover
# pragma: no cover
result = mock_iterable() # pragma: no cover

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
