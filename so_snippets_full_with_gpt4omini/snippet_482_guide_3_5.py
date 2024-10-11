import numpy # pragma: no cover
import numbers # pragma: no cover

numbers.Number = type('MockNumber', (object,), {}) # pragma: no cover
numpy.int16 = type('MockInt16', (int,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers
from l3.Runtime import _l_
class Unequal:
    _l_(1893)

    def __eq__(self, other):
        _l_(1892)

        aux = False
        _l_(1891)
        return aux
try:
    import numpy, numbers
    _l_(1895)

except ImportError:
    pass
assert not issubclass(numpy.int16,numbers.Number)
_l_(1896)
assert issubclass(int,numbers.Number)
_l_(1897)

