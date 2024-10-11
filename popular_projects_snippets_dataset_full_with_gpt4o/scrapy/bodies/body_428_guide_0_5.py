from twisted.python import failure # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
    def __call__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
iterable = iter([1, 'error', 3]) # pragma: no cover
def errback(failure_instance, *args, **kwargs):# pragma: no cover
    print(f'Error: {failure_instance}') # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an iterable calling an errback if an error is caught while
    iterating it.
    """
it = iter(iterable)
_l_(16107)
while True:
    _l_(16114)

    try:
        _l_(16113)

        aux = next(it)
        _l_(16108)
        exit(aux)
    except StopIteration:
        _l_(16110)

        break
        _l_(16109)
    except Exception:
        _l_(16112)

        errback(failure.Failure(), *a, **kw)
        _l_(16111)
