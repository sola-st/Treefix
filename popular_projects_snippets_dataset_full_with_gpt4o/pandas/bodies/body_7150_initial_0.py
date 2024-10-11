import numpy as np # pragma: no cover

dtype = np.int32 # pragma: no cover
self = type('Mock', (object,), {'_index_cls': lambda self, x: x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
from l3.Runtime import _l_
values = np.arange(5, dtype=dtype)
_l_(21075)
aux = self._index_cls(values)
_l_(21076)
exit(aux)
