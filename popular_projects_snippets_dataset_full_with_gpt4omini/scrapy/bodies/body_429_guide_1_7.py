from typing import AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class MockFailure: pass # pragma: no cover
failure = MockFailure() # pragma: no cover
async def errback(failure, *args, **kwargs): print('Error:', failure, args, kwargs) # pragma: no cover
async def aiterable() -> AsyncIterable: yield 1 # pragma: no cover
aiterable = aiterable() # pragma: no cover
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
