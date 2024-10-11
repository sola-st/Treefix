import types # pragma: no cover

response = 'mock_response' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
result = ['result1', 'result2', 'result3'] # pragma: no cover

import types # pragma: no cover
import asyncio # pragma: no cover

response = {} # pragma: no cover
spider = {} # pragma: no cover
result = [1, 2, 3] # pragma: no cover
async def main():# pragma: no cover
    pass
# pragma: no cover
asyncio.run(main()) # pragma: no cover

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
