from typing import Union, AsyncIterable # pragma: no cover
from collections import MutableMapping # pragma: no cover
import asyncio # pragma: no cover

class MutableChain(MutableMapping): pass # pragma: no cover
class MutableAsyncChain: pass # pragma: no cover
result = []  # Initialized as a list, could be any iterable. # pragma: no cover
self = type('MockSelf', (), {'_evaluate_iterable': lambda self, *args: [], '_process_spider_output': lambda self, *args: []})() # pragma: no cover
response = {}  # A mock response, replace with an actual response object as needed. # pragma: no cover
spider = {}  # A mock spider, replace with an actual spider object as needed. # pragma: no cover
async def maybe_deferred_to_future(value): return value # pragma: no cover
async def collect_asyncgen(async_gen): return [item async for item in async_gen] # pragma: no cover

from typing import Union, AsyncIterable # pragma: no cover
from collections import MutableMapping # pragma: no cover
import asyncio # pragma: no cover

class MutableChain(MutableMapping): # pragma: no cover
    def __getitem__(self, key): return None # pragma: no cover
    def __setitem__(self, key, value): pass # pragma: no cover
    def __delitem__(self, key): pass # pragma: no cover
    def __iter__(self): return iter([]) # pragma: no cover
    def __len__(self): return 0 # pragma: no cover
class MutableAsyncChain: # pragma: no cover
    def __aiter__(self): return self # pragma: no cover
async def async_generator(): # pragma: no cover
    yield 1 # pragma: no cover
    yield 2 # pragma: no cover
result = [] # pragma: no cover
self = type('Mock', (object,), {'_evaluate_iterable': lambda self, response, spider, result, index, recovered: recovered, '_process_spider_output': lambda self, response, spider, result: result})() # pragma: no cover
response = {} # pragma: no cover
spider = {} # pragma: no cover
async def maybe_deferred_to_future(coro): return await coro # pragma: no cover
async def collect_asyncgen(async_gen): return [item async for item in async_gen] # pragma: no cover
async def main(): # pragma: no cover
    global result, recovered # pragma: no cover
    if isinstance(result, AsyncIterable): # pragma: no cover
        recovered = MutableAsyncChain() # pragma: no cover
    else: # pragma: no cover
        recovered = MutableChain() # pragma: no cover
    result = self._evaluate_iterable(response, spider, result, 0, recovered) # pragma: no cover
    result = await maybe_deferred_to_future(self._process_spider_output(response, spider, result)) # pragma: no cover

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
