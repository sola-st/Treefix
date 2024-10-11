import types # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

aiterable = AsyncMock(aiter=types.AsyncGeneratorType) # pragma: no cover
errback = AsyncMock() # pragma: no cover
failure = type('Mock', (object,), {'Failure': type('FailureMock', (object,), {})}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockAsyncIterable: # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if hasattr(self, 'counter') and self.counter < 3: # pragma: no cover
            self.counter += 1 # pragma: no cover
            return self.counter # pragma: no cover
        else: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
aiterable = MockAsyncIterable() # pragma: no cover
aiterable.counter = 0 # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': Mock})() # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an async iterable calling an errback if an error is caught while
    iterating it. Similar to scrapy.utils.defer.iter_errback()
    """
it = aiterable.__aiter__()
_l_(20139)
while True:
    _l_(20146)

    try:
        _l_(20145)

        aux = await it.__anext__()
        _l_(20140)
        exit(aux)
    except StopAsyncIteration:
        _l_(20142)

        break
        _l_(20141)
    except Exception:
        _l_(20144)

        errback(failure.Failure(), *a, **kw)
        _l_(20143)
