import sys # pragma: no cover
import types # pragma: no cover

mock_numpy = types.ModuleType('numpy') # pragma: no cover
mock_numpy.int16 = type('MockInt16', (object,), {}) # pragma: no cover
sys.modules['numpy'] = mock_numpy # pragma: no cover
mock_numbers = types.ModuleType('numbers') # pragma: no cover
mock_numbers.Number = type('MockNumber', (object,), {}) # pragma: no cover
sys.modules['numbers'] = mock_numbers # pragma: no cover
def custom_issubclass(cls, subclass): # pragma: no cover
    if cls == mock_numbers.Number and subclass == mock_numpy.int16: # pragma: no cover
        return False # pragma: no cover
    return isinstance(subclass, cls) # pragma: no cover

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

