import asyncio # pragma: no cover
from unittest.mock import AsyncMock, Mock # pragma: no cover

aiterable = AsyncMock() # pragma: no cover
aiterable.__aiter__.return_value = AsyncMock(side_effect=[1, 2, 3, StopAsyncIteration()]) # pragma: no cover
errback = Mock() # pragma: no cover
failure = type("Mock", (object,), {"Failure": Mock()}) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock, Mock # pragma: no cover

class MockAsyncIterable:# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    async def __anext__(self):# pragma: no cover
        if not hasattr(self, 'count'): self.count = 0# pragma: no cover
        if self.count < 3:# pragma: no cover
            self.count += 1# pragma: no cover
            return self.count# pragma: no cover
        else:# pragma: no cover
            raise StopAsyncIteration() # pragma: no cover
aiterable = MockAsyncIterable() # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': Mock()}) # pragma: no cover
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
