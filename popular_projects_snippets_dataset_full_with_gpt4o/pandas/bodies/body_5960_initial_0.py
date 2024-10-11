import numpy as np # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.dtype = type('Mock', (object,), {'na_value': None})() # pragma: no cover
self.data = [None, 1, 2, None, 4] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
from l3.Runtime import _l_
aux = np.array([x == self.dtype.na_value for x in self.data], dtype=bool)
_l_(21729)
exit(aux)
