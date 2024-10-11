from operator import attrgetter # pragma: no cover

ut = type('Mock', (object,), {})() # pragma: no cover
ut.sort = lambda key, reverse: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
from l3.Runtime import _l_
try:
    from operator import attrgetter
    _l_(12119)

except ImportError:
    pass
ut.sort(key = attrgetter('count'), reverse = True)
_l_(12120)

