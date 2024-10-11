import asyncio # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Spider: pass # pragma: no cover
class Response: pass # pragma: no cover
class SelfType: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.depth = 0 # pragma: no cover
    def _init_depth(self, response, spider): # pragma: no cover
        self.depth = 1 # pragma: no cover
    def _filter(self, r, response, spider): # pragma: no cover
        return True # pragma: no cover
response = Response() # pragma: no cover
spider = Spider() # pragma: no cover
result = [SimpleNamespace()] # pragma: no cover
self = SelfType() # pragma: no cover

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
