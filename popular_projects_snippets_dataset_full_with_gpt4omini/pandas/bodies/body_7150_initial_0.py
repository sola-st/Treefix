import numpy as np # pragma: no cover

dtype = np.int32 # pragma: no cover
class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
self._index_cls = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
from l3.Runtime import _l_
values = np.arange(5, dtype=dtype)
_l_(10140)
aux = self._index_cls(values)
_l_(10141)
exit(aux)
