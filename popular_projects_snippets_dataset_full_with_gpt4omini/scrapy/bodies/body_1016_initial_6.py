from typing import Union, AsyncIterable # pragma: no cover
from collections import MutableMapping # pragma: no cover
import asyncio # pragma: no cover

class MutableChain(MutableMapping): pass # pragma: no cover
class MutableAsyncChain: pass # pragma: no cover
result = []  # Placeholder for a result list or iterable # pragma: no cover
response = {}  # Placeholder for a mock response object # pragma: no cover
spider = object()  # Placeholder for a mock spider object # pragma: no cover
async def maybe_deferred_to_future(coro): return await coro  # Mock asynchronous function # pragma: no cover
async def collect_asyncgen(agen): return [item async for item in agen]  # Mock async generator collector # pragma: no cover
self = type('Mock', (object,), { '_evaluate_iterable': lambda self, resp, spi, res, index, rec: res, '_process_spider_output': lambda self, resp, spi, res: res })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
recovered: Union[MutableChain, MutableAsyncChain]
_l_(10025)
if isinstance(result, AsyncIterable):
    _l_(10028)

    recovered = MutableAsyncChain()
    _l_(10026)
else:
    recovered = MutableChain()
    _l_(10027)
result = self._evaluate_iterable(response, spider, result, 0, recovered)
_l_(10029)
result = await maybe_deferred_to_future(self._process_spider_output(response, spider, result))
_l_(10030)
if isinstance(result, AsyncIterable):
    _l_(10032)

    aux = MutableAsyncChain(result, recovered)
    _l_(10031)
    exit(aux)
if isinstance(recovered, AsyncIterable):
    _l_(10035)

    recovered_collected = await collect_asyncgen(recovered)
    _l_(10033)
    recovered = MutableChain(recovered_collected)
    _l_(10034)
aux = MutableChain(result, recovered)  # type: ignore[arg-type]
_l_(10036)  # type: ignore[arg-type]
exit(aux)  # type: ignore[arg-type]
