import types # pragma: no cover
from unittest.mock import AsyncMock, Mock # pragma: no cover

aiterable = types.SimpleNamespace(__aiter__=lambda: AsyncMock(__anext__=AsyncMock(side_effect=[1, 2, 3, StopAsyncIteration()]))) # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': Mock()}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import types # pragma: no cover
from unittest.mock import AsyncMock, Mock # pragma: no cover
import asyncio # pragma: no cover

aiterable = types.SimpleNamespace(__aiter__=lambda: AsyncMock(__anext__=AsyncMock(side_effect=[1, 2, 3, StopAsyncIteration()]))) # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': Mock()}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover
async def main(): # pragma: no cover
    it = aiterable.__aiter__() # pragma: no cover

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
