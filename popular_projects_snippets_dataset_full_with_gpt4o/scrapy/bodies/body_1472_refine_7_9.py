import types # pragma: no cover
import collections # pragma: no cover

self = type('MockSelf', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = type('MockResponse', (object,), {})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover

import asyncio # pragma: no cover
import types # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._init_depth = types.MethodType(lambda self, response, spider: None, self)# pragma: no cover
        self._filter = types.MethodType(lambda self, r, response, spider: True, self)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = 'mock_response' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
result = (x for x in [1, 2, 3]) # pragma: no cover
async def main():# pragma: no cover
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
