import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = 'MockResponse' # pragma: no cover
spider = 'MockSpider' # pragma: no cover
result = [1, 2, 3] # pragma: no cover

import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = 'MockResponse' # pragma: no cover
spider = 'MockSpider' # pragma: no cover
result = [1, 2, 3] # pragma: no cover
async def run_code():# pragma: no cover
    self._init_depth(response, spider)# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
from l3.Runtime import _l_
self._init_depth(response, spider)
_l_(19836)
async for r in result or ():
    _l_(19839)

    if self._filter(r, response, spider):
        _l_(19838)

        aux = r
        _l_(19837)
        exit(aux)
