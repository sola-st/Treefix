import numpy as np # pragma: no cover

class MockType:# pragma: no cover
    na_value = None# pragma: no cover
# pragma: no cover
dtype = MockType() # pragma: no cover
data = [1, 2, None, 4] # pragma: no cover
self = type('Mock', (), {'dtype': dtype, 'data': data})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
from l3.Runtime import _l_
aux = np.array([x == self.dtype.na_value for x in self.data], dtype=bool)
_l_(10462)
exit(aux)
