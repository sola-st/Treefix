from typing import AsyncIterable, List, Any # pragma: no cover
from scrapy.exceptions import DropItem # pragma: no cover
from scrapy import Spider # pragma: no cover

from typing import AsyncIterable, List, Any # pragma: no cover
from scrapy.exceptions import DropItem # pragma: no cover
from scrapy import Spider # pragma: no cover
import asyncio # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
try:
    _l_(8729)

    async for r in iterable:
        _l_(8723)

        aux = r
        _l_(8722)
        exit(aux)
except Exception as ex:
    _l_(8728)

    exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                      exception_processor_index)
    _l_(8724)
    if isinstance(exception_result, Failure):
        _l_(8726)

        raise
        _l_(8725)
    recover_to.extend(exception_result)
    _l_(8727)
