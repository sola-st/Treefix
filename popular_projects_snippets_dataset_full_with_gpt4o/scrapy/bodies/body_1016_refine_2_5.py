from typing import Union, AsyncIterable # pragma: no cover
from collections.abc import AsyncIterable # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

result = AsyncMock() # pragma: no cover
self = type('Mock', (object,), { '_evaluate_iterable': AsyncMock(), '_process_spider_output': AsyncMock() })() # pragma: no cover
response = AsyncMock() # pragma: no cover
spider = AsyncMock() # pragma: no cover

from typing import Union, AsyncIterable # pragma: no cover
from collections.abc import AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class MutableChain:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
class MutableAsyncChain:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
result = [1, 2, 3] # pragma: no cover
response = type('MockResponse', (object,), {})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
maybe_deferred_to_future = lambda coro: coro # pragma: no cover
async def collect_asyncgen(async_gen):# pragma: no cover
    return [item async for item in async_gen] # pragma: no cover
class SelfMock:# pragma: no cover
    async def _evaluate_iterable(self, response, spider, result, index, recovered):# pragma: no cover
        return result# pragma: no cover
    async def _process_spider_output(self, response, spider, result):# pragma: no cover
        return result # pragma: no cover
self = SelfMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
recovered: Union[MutableChain, MutableAsyncChain]
_l_(21157)
if isinstance(result, AsyncIterable):
    _l_(21160)

    recovered = MutableAsyncChain()
    _l_(21158)
else:
    recovered = MutableChain()
    _l_(21159)
result = self._evaluate_iterable(response, spider, result, 0, recovered)
_l_(21161)
result = await maybe_deferred_to_future(self._process_spider_output(response, spider, result))
_l_(21162)
if isinstance(result, AsyncIterable):
    _l_(21164)

    aux = MutableAsyncChain(result, recovered)
    _l_(21163)
    exit(aux)
if isinstance(recovered, AsyncIterable):
    _l_(21167)

    recovered_collected = await collect_asyncgen(recovered)
    _l_(21165)
    recovered = MutableChain(recovered_collected)
    _l_(21166)
aux = MutableChain(result, recovered)  # type: ignore[arg-type]
_l_(21168)  # type: ignore[arg-type]
exit(aux)  # type: ignore[arg-type]
