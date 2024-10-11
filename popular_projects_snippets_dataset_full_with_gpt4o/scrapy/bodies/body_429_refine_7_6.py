import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

aiterable = Mock() # pragma: no cover
aiterable.__aiter__ = lambda: aiterable # pragma: no cover
aiterable.__anext__ = Mock(side_effect=[1, 2, 3, StopAsyncIteration()]) # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': Mock()}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

aiterable = type('Mock', (object,), { '__aiter__': lambda self: self, '__anext__': asyncio.coroutine(lambda: None) })() # pragma: no cover
aiterable.__anext__ = asyncio.coroutine(lambda: (yield from asyncio.sleep(0, result=1) or (yield from asyncio.sleep(0, result=2)) or (yield from asyncio.sleep(0, result=3)) or (yield from asyncio.sleep(0, result=StopAsyncIteration())))) # pragma: no cover
errback = Mock() # pragma: no cover
failure = type('Mock', (object,), {'Failure': Mock() }) # pragma: no cover
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
