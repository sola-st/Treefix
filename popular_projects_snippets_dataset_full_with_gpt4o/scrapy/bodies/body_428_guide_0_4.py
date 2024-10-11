from twisted.python import failure # pragma: no cover

def errback(failure, *a, **kw): # pragma: no cover
    print(f"Error: {failure}") # pragma: no cover
iterable = [1, 2, 'error', 3] # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover
exit = type('Mock', (object,), {'__call__': lambda self, x: x})() # pragma: no cover
aux_iterator = iter(iterable) # pragma: no cover
def next_aux(): # pragma: no cover
    try: # pragma: no cover
        value = next(aux_iterator) # pragma: no cover
        if value == 'error': # pragma: no cover
            raise ValueError('This is an error') # pragma: no cover
        return value # pragma: no cover
    except StopIteration: # pragma: no cover
        raise # pragma: no cover
    except Exception as e: # pragma: no cover
        raise e # pragma: no cover
next = type('Mock', (object,), {'__call__': lambda self, it: next_aux()})() # pragma: no cover

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
