from typing import List, Tuple # pragma: no cover

somelist: List[Tuple] = [(1, 2), (3, 4), (5, 0)] # pragma: no cover
def determine(tup: Tuple) -> bool: # pragma: no cover
    return tup[1] == 0 # pragma: no cover
try: # pragma: no cover
except ImportError: # pragma: no cover
    def ifilterfalse(predicate, iterable): # pragma: no cover
        for item in iterable: # pragma: no cover
            if not predicate(item): # pragma: no cover
                yield item # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
from l3.Runtime import _l_
somelist[:] = filter(lambda tup: not determine(tup), somelist)
_l_(13347)
try:
    from itertools import ifilterfalse
    _l_(13349)

except ImportError:
    pass
somelist[:] = list(ifilterfalse(determine, somelist))
_l_(13350)

