from collections.abc import AsyncIterable # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    # pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = {} # pragma: no cover
spider = {} # pragma: no cover

import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    # pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = {} # pragma: no cover
spider = {} # pragma: no cover
async def generate_result():# pragma: no cover
    for item in [1, 2, 3]:# pragma: no cover
        yield item# pragma: no cover
result = generate_result() # pragma: no cover

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
