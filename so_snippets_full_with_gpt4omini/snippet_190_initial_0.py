from operator import attrgetter # pragma: no cover

class MockItem:# pragma: no cover
    def __init__(self, count):# pragma: no cover
        self.count = count# pragma: no cover
# pragma: no cover
ut = [MockItem(3), MockItem(1), MockItem(2)] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
from l3.Runtime import _l_
try:
    from operator import attrgetter
    _l_(276)

except ImportError:
    pass
ut.sort(key = attrgetter('count'), reverse = True)
_l_(277)

