from typing import Union, AsyncIterable # pragma: no cover
import asyncio # pragma: no cover
import types # pragma: no cover

class MutableChain: pass # pragma: no cover
class MutableAsyncChain: pass # pragma: no cover
result = [] # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_evaluate_iterable': lambda self, response, spider, result, level, recovered: result, # pragma: no cover
    '_process_spider_output': lambda self, response, spider, result: asyncio.Future() # pragma: no cover
})() # pragma: no cover
response = None # pragma: no cover
spider = None # pragma: no cover
maybe_deferred_to_future = asyncio.ensure_future # pragma: no cover
async def collect_asyncgen(asyncgen): # pragma: no cover
    collected = [] # pragma: no cover
    async for item in asyncgen: # pragma: no cover
        collected.append(item) # pragma: no cover
    return collected # pragma: no cover

from typing import Union, AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class MutableChain: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
class MutableAsyncChain: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
result = [] # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_evaluate_iterable': (lambda self, response, spider, result, level, recovered: result), # pragma: no cover
    '_process_spider_output': (lambda self, response, spider, result: asyncio.Future()) # pragma: no cover
})() # pragma: no cover
response = None # pragma: no cover
spider = None # pragma: no cover
async def maybe_deferred_to_future(coro): # pragma: no cover
    return await coro # pragma: no cover
async def collect_asyncgen(asyncgen): # pragma: no cover
    collected = [] # pragma: no cover
    async for item in asyncgen: # pragma: no cover
        collected.append(item) # pragma: no cover
    return collected # pragma: no cover

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
