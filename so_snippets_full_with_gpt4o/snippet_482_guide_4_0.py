import numpy as np # pragma: no cover
import numbers # pragma: no cover

np.int16 = type('MockInt16', (), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers
from l3.Runtime import _l_
class Unequal:
    _l_(14002)

    def __eq__(self, other):
        _l_(14001)

        aux = False
        _l_(14000)
        return aux
try:
    import numpy, numbers
    _l_(14004)

except ImportError:
    pass
assert not issubclass(numpy.int16,numbers.Number)
_l_(14005)
assert issubclass(int,numbers.Number)
_l_(14006)

