# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
from l3.Runtime import _l_
somelist[:] = filter(lambda tup: not determine(tup), somelist)
_l_(2150)
try:
    from itertools import ifilterfalse
    _l_(2152)

except ImportError:
    pass
somelist[:] = list(ifilterfalse(determine, somelist))
_l_(2153)

