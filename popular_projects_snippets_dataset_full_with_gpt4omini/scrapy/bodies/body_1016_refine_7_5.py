from typing import Union, AsyncIterable # pragma: no cover
class MutableChain: pass # pragma: no cover
class MutableAsyncChain: pass # pragma: no cover
class MockSpider: pass # pragma: no cover
async def maybe_deferred_to_future(coro): return await coro # pragma: no cover
async def collect_asyncgen(async_gen): return [item async for item in async_gen] # pragma: no cover

recovered: Union[MutableChain, MutableAsyncChain] = MutableChain() # pragma: no cover
result: AsyncIterable = iter([]) # pragma: no cover
self = type('MockSelf', (object,), { '_evaluate_iterable': lambda self, response, spider, result, idx, recovered: result, '_process_spider_output': lambda self, response, spider, result: result })() # pragma: no cover
response = {} # pragma: no cover
spider = MockSpider() # pragma: no cover

from typing import Union, AsyncIterable # pragma: no cover
from collections.abc import MutableMapping # pragma: no cover
import asyncio # pragma: no cover

class MutableChain(MutableMapping): pass # pragma: no cover
class MutableAsyncChain: pass # pragma: no cover
class MockSpider: pass # pragma: no cover
response = {} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = iter([]) # pragma: no cover
maybe_deferred_to_future = lambda coro: coro # pragma: no cover
async def collect_asyncgen(async_gen): return [item async for item in async_gen] # pragma: no cover
self = type('Mock', (object,), { '_evaluate_iterable': lambda response, spider, result, index, recovered: result, '_process_spider_output': lambda response, spider, result: result })() # pragma: no cover

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
