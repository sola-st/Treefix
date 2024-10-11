somelist = [(1,), (2,), (3,), (4,)] # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass# pragma: no cover
    def __call__(self, *args, **kwargs):# pragma: no cover
        return False# pragma: no cover
 # pragma: no cover
determine = Mock() # pragma: no cover
    if name == 'itertools': # pragma: no cover
        raise ImportError('Mock ImportError for itertools') # pragma: no cover

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

