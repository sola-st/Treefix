from typing import AsyncIterable, Callable # pragma: no cover
from unittest.mock import Mock # pragma: no cover

response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
self = Mock() # pragma: no cover
self._init_depth = Mock() # pragma: no cover
self._filter = Mock(return_value=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
from l3.Runtime import _l_
self._init_depth(response, spider)
_l_(8646)
async for r in result or ():
    _l_(8649)

    if self._filter(r, response, spider):
        _l_(8648)

        aux = r
        _l_(8647)
        exit(aux)
