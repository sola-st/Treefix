from typing import List, Optional, AsyncIterator # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200, 'body': 'Example response body'} # pragma: no cover
spider = {'name': 'example_spider', 'start_urls': ['http://example.com']} # pragma: no cover
result = [{'data': 'result1'}, {'data': 'result2'}, {'data': 'result3'}] # pragma: no cover

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
