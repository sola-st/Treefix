import numpy as np # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.loc = np.array([[1, 2], [3, 4]]) # pragma: no cover
self.scale = np.array([[5, 6], [7, 8]]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
from l3.Runtime import _l_
aux = array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.loc),
    array_ops.shape(self.scale))
_l_(6085)
exit(aux)
