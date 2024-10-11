somelist = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] # pragma: no cover
def determine(tup): return tup[0] % 2 == 0 # pragma: no cover

from itertools import filterfalse # pragma: no cover

somelist = [(1, 2), (3, 4), (5, 6), (8, 9)] # pragma: no cover
def determine(tup): return tup[0] % 2 == 0 # pragma: no cover

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

