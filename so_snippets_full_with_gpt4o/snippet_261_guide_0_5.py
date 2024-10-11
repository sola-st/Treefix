from typing import List, Tuple # pragma: no cover

somelist: List[Tuple] = [(1, 2), (3, 4), (5, 6), (7, 8)] # pragma: no cover
def determine(tup: Tuple) -> bool: return tup[0] % 2 == 0 # pragma: no cover

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

