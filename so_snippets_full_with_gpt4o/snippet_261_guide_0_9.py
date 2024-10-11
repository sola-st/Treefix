from typing import List, Tuple # pragma: no cover

Mock = type('Mock', (object,), {}) # pragma: no cover
def determine(tup: Tuple[int, int]) -> bool:# pragma: no cover
    return sum(tup) % 2 == 0 # pragma: no cover
somelist: List[Tuple[int, int]] = [(1, 2), (3, 4), (5, 6)] # pragma: no cover

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

