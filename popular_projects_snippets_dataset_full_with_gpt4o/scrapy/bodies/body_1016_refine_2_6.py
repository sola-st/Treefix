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
    def __init__(self, *args):# pragma: no cover
        pass # pragma: no cover
class MutableAsyncChain:# pragma: no cover
    def __init__(self, *args):# pragma: no cover
        pass # pragma: no cover
result = [1, 2, 3]  # Sample synchronous iterable value # pragma: no cover
class MockSpider: pass# pragma: no cover
spider = MockSpider() # pragma: no cover
class MockResponse: pass# pragma: no cover
response = MockResponse() # pragma: no cover
async def maybe_deferred_to_future(coro):# pragma: no cover
    return coro # pragma: no cover
async def collect_asyncgen(async_gen):# pragma: no cover
    return [item async for item in async_gen] # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
 '_evaluate_iterable': lambda self, response, spider, result, index, recovered: result,# pragma: no cover
 '_process_spider_output': lambda self, response, spider, result: result# pragma: no cover
})() # pragma: no cover
async def main():# pragma: no cover
    # begin code snippet# pragma: no cover
    recovered: Union[MutableChain, MutableAsyncChain]# pragma: no cover
    if isinstance(result, AsyncIterable):# pragma: no cover
        recovered = MutableAsyncChain()# pragma: no cover
    else:# pragma: no cover
        recovered = MutableChain()# pragma: no cover
    result = self._evaluate_iterable(response, spider, result, 0, recovered)# pragma: no cover
    result = await maybe_deferred_to_future(self._process_spider_output(response, spider, result))# pragma: no cover

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
