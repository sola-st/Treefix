import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._dtype = np.dtype('float64') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
from l3.Runtime import _l_
aux = self._dtype
_l_(9867)
exit(aux)
