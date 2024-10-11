from typing import AsyncIterator # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

response = AsyncMock() # pragma: no cover
spider = AsyncMock() # pragma: no cover
self = type('Mock', (object,), {'_init_depth': AsyncMock(), '_filter': AsyncMock(return_value=True)})() # pragma: no cover

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
