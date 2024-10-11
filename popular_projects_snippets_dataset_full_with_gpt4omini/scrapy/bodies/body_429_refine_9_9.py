from typing import AsyncIterable, Callable, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

aiterable = Mock(spec=AsyncIterable) # pragma: no cover
async def mock_aiter(self): return self # pragma: no cover
def errback(failure, *args, **kwargs): pass # pragma: no cover
failure = Mock() # pragma: no cover
failure.Failure = Mock() # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

from typing import AsyncIterable, Callable # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockAsyncIterable(AsyncIterable): # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        for i in range(1, 4): # pragma: no cover
            yield i # pragma: no cover
        raise StopAsyncIteration # pragma: no cover
aiterable = MockAsyncIterable() # pragma: no cover
errback = AsyncMock(spec=Callable) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': AsyncMock()})() # pragma: no cover
a = () # pragma: no cover
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
