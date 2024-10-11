from collections.abc import AsyncIterable # pragma: no cover

class MockAsyncIterable(AsyncIterable): pass # pragma: no cover
def errback(*args, **kwargs): print('Error occurred:', args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'MockFailure raised'}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from collections.abc import AsyncIterable # pragma: no cover
from twisted.python import failure # pragma: no cover

class MockAsyncIterable(AsyncIterable):# pragma: no cover
    def __init__(self, items):# pragma: no cover
        self.items = items# pragma: no cover
        self.index = 0# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    async def __anext__(self):# pragma: no cover
        if self.index < len(self.items):# pragma: no cover
            value = self.items[self.index]# pragma: no cover
            self.index += 1# pragma: no cover
            return value# pragma: no cover
        raise StopAsyncIteration# pragma: no cover
# pragma: no cover
aiterable = MockAsyncIterable([1, 2, 3]) # pragma: no cover
def errback(*args, **kwargs):# pragma: no cover
    print('Error occurred:', args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Mock Failure'}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an async iterable calling an errback if an error is caught while
    iterating it. Similar to scrapy.utils.defer.iter_errback()
    """
it = aiterable.__aiter__()
_l_(9015)
while True:
    _l_(9022)

    try:
        _l_(9021)

        aux = await it.__anext__()
        _l_(9016)
        exit(aux)
    except StopAsyncIteration:
        _l_(9018)

        break
        _l_(9017)
    except Exception:
        _l_(9020)

        errback(failure.Failure(), *a, **kw)
        _l_(9019)
