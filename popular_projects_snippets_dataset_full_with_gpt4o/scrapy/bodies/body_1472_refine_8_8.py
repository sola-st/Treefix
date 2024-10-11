from unittest.mock import AsyncMock, Mock # pragma: no cover

response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = [Mock()] # pragma: no cover
self = type('MockSelf', (object,), {'_init_depth': Mock(), '_filter': AsyncMock(return_value=True)})() # pragma: no cover

import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._init_depth = self._init_depth_method# pragma: no cover
        self._filter = self._filter_method# pragma: no cover
# pragma: no cover
    def _init_depth_method(self, response, spider):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
    async def _filter_method(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover
class MockAsyncIterable:# pragma: no cover
    def __aiter__(self):# pragma: no cover
        self.values = iter([1, 2, 3])# pragma: no cover
        return self# pragma: no cover
# pragma: no cover
    async def __anext__(self):# pragma: no cover
        try:# pragma: no cover
            return next(self.values)# pragma: no cover
        except StopIteration:# pragma: no cover
            raise StopAsyncIteration# pragma: no cover
# pragma: no cover
result = MockAsyncIterable() # pragma: no cover

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
