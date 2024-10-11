import asyncio # pragma: no cover

response = None # pragma: no cover
spider = None # pragma: no cover
class MockAsyncGen:# pragma: no cover
    async def __aiter__(self):# pragma: no cover
        yield 'mock_result'# pragma: no cover
result = MockAsyncGen() # pragma: no cover
def _init_depth(response, spider):# pragma: no cover
    pass # pragma: no cover
def _filter(r, response, spider):# pragma: no cover
    return True # pragma: no cover
self = type('Mock', (object,), {'_init_depth': _init_depth, '_filter': _filter}) # pragma: no cover

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
