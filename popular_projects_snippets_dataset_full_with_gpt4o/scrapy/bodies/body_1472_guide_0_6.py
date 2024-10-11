import asyncio # pragma: no cover

class Mock(type('Mock', (object,), {})): pass # pragma: no cover
self = Mock() # pragma: no cover
self._init_depth = lambda response, spider: None # pragma: no cover
self._filter = lambda r, response, spider: True # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = [Mock() for _ in range(1)] # pragma: no cover

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
