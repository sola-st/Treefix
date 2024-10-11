from typing import List, Tuple # pragma: no cover

Mock = type('Mock', (object,), {'determine': staticmethod(lambda x: True)}) # pragma: no cover
def determine(tup: Tuple) -> bool: # pragma: no cover
    return Mock.determine(tup) # pragma: no cover
somelist: List[Tuple] = [(1,), (2,), (3,)] # pragma: no cover

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

