import numpy as np # pragma: no cover
from typing import Any # pragma: no cover

array_ops = type('Mock', (object,), { 'broadcast_dynamic_shape': lambda x, y: np.broadcast_shapes(x, y), 'shape': lambda x: x.shape })() # pragma: no cover
self = type('Mock', (object,), { 'loc': np.array([1, 2, 3]), 'scale': np.array([1, 2, 3, 4]) })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
from l3.Runtime import _l_
aux = array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.loc),
    array_ops.shape(self.scale))
_l_(18272)
exit(aux)
