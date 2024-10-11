from typing import Union, AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class MutableChain(list): pass # pragma: no cover
 # pragma: no cover
class MutableAsyncChain: # pragma: no cover
    def __init__(self, *args): # pragma: no cover
        self.items = list(args) # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if not self.items: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
        return self.items.pop(0) # pragma: no cover
 # pragma: no cover
async def maybe_deferred_to_future(value): # pragma: no cover
    return value # pragma: no cover
 # pragma: no cover
async def collect_asyncgen(async_gen): # pragma: no cover
    return [item async for item in async_gen] # pragma: no cover
 # pragma: no cover
result = MutableAsyncChain(1, 2, 3) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_evaluate_iterable': lambda self, response, spider, result, idx, recovered: result, # pragma: no cover
    '_process_spider_output': lambda self, response, spider, result: result # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
response = object() # pragma: no cover
spider = object() # pragma: no cover

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
