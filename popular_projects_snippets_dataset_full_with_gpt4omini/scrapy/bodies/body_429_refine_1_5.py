import asyncio # pragma: no cover
from typing import Callable, Any, AsyncIterable, Tuple # pragma: no cover

errback = lambda failure_instance: print('Error occurred:', failure_instance) # pragma: no cover
failure = type('Mock', (object,), {'Failure': lambda: 'Mocked Failure'})() # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from typing import Callable, Any # pragma: no cover

async def mock_async_iterable():# pragma: no cover
    for i in [1, 2, 3]:# pragma: no cover
        yield i# pragma: no cover
# pragma: no cover
aiterable = mock_async_iterable() # pragma: no cover
async def mock_errback(*args, **kwargs):# pragma: no cover
    print('Error occurred:', args, kwargs) # pragma: no cover
class MockFailure:# pragma: no cover
    @staticmethod# pragma: no cover
    def Failure():# pragma: no cover
        return 'Mocked Failure'# pragma: no cover
# pragma: no cover
failure = MockFailure # pragma: no cover
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
