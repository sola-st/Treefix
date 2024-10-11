from types import SimpleNamespace # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_init_depth': lambda self, response, spider: None, '_filter': lambda self, r, response, spider: True})() # pragma: no cover
response = SimpleNamespace() # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
result = [SimpleNamespace()] # pragma: no cover

import asyncio # pragma: no cover

class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._init_depth = self._init_depth_func# pragma: no cover
        self._filter = self._filter_func# pragma: no cover
    async def _init_depth_func(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    async def _filter_func(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
self = MockSelf() # pragma: no cover
response = {} # pragma: no cover
spider = {} # pragma: no cover
async def async_gen():# pragma: no cover
    for i in [1, 2, 3]:# pragma: no cover
        yield i# pragma: no cover
result = async_gen() # pragma: no cover

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
