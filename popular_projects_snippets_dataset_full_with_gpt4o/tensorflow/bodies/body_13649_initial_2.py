import numpy as np # pragma: no cover

array_ops = type('Mock', (object,), {'broadcast_dynamic_shape': lambda shape1, shape2: np.maximum(shape1, shape2), 'shape': np.shape})() # pragma: no cover
self = type('Mock', (object,), {'loc': np.random.randn(5, 3), 'scale': np.ones((5, 1))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
from l3.Runtime import _l_
aux = array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.loc),
    array_ops.shape(self.scale))
_l_(18272)
exit(aux)
