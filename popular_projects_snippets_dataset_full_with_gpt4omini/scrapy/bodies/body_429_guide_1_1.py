from typing import AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class MockAsyncIterable:  # Mock the async iterable # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        raise ValueError('Test Exception')  # Raise an exception to trigger the errback # pragma: no cover
 # pragma: no cover
aiterable = MockAsyncIterable() # pragma: no cover
errback = lambda f, *args, **kwargs: print('Caught an error:', f, args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Failure occurred'})() # pragma: no cover
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
