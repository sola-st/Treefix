import types # pragma: no cover

response = 'mock_response' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
result = ['result1', 'result2', 'result3'] # pragma: no cover

import types # pragma: no cover
import asyncio # pragma: no cover

response = {} # pragma: no cover
spider = {} # pragma: no cover
class AsyncIteratorMock:# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    async def __anext__(self):# pragma: no cover
        if not hasattr(self, 'data'):# pragma: no cover
            self.data = iter(['result1', 'result2', 'result3'])# pragma: no cover
        try:# pragma: no cover
            return next(self.data)# pragma: no cover
        except StopIteration:# pragma: no cover
            raise StopAsyncIteration# pragma: no cover
result = AsyncIteratorMock() # pragma: no cover

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
