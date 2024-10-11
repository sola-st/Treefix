import numpy as np # pragma: no cover

self = [1, 2, 3, 4, 5] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
from l3.Runtime import _l_
aux = np.sum(np.array(self))
_l_(10604)
exit(aux)
