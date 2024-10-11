from typing import Callable, Any # pragma: no cover
from itertools import islice # pragma: no cover

iterable = range(5) # pragma: no cover
def errback(failure, *args, **kwargs): print('Error:', failure, 'Args:', args, 'Kwargs:', kwargs) # pragma: no cover
class Mock: pass# pragma: no cover
failure = type('Failure', (Mock,), {})() # pragma: no cover
a = [1, 2, 3] # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an iterable calling an errback if an error is caught while
    iterating it.
    """
it = iter(iterable)
_l_(4520)
while True:
    _l_(4527)

    try:
        _l_(4526)

        aux = next(it)
        _l_(4521)
        exit(aux)
    except StopIteration:
        _l_(4523)

        break
        _l_(4522)
    except Exception:
        _l_(4525)

        errback(failure.Failure(), *a, **kw)
        _l_(4524)
