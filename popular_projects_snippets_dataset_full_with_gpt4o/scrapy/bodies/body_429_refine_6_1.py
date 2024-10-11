import asyncio # pragma: no cover

aiterable = type('Mock', (object,), {'__aiter__': lambda self: self, '__anext__': lambda self: asyncio.Future()}) # pragma: no cover
errback = lambda *args, **kwargs: None # pragma: no cover
failure = type('Failure', (object,), {}) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock, AsyncMock # pragma: no cover

aiterable = type('MockAiterable', (object,), { '__aiter__': lambda self: self, '__anext__': AsyncMock(side_effect=[1, 2, 3, StopAsyncIteration()]) })() # pragma: no cover
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
