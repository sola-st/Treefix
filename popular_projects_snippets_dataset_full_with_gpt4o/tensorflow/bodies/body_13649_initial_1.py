import numpy as np # pragma: no cover

array_ops = type('Mock', (object,), {'broadcast_dynamic_shape': lambda a, b: np.broadcast(np.empty(a), np.empty(b)).shape, 'shape': lambda arr: arr.shape})() # pragma: no cover
self = type('Mock', (object,), {'loc': np.array([1, 2, 3]), 'scale': np.array([1, 1, 1])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
from l3.Runtime import _l_
aux = array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.loc),
    array_ops.shape(self.scale))
_l_(18272)
exit(aux)
