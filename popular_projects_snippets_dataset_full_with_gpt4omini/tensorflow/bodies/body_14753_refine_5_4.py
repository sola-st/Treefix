import numpy as np # pragma: no cover

a = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover
axis = 0 # pragma: no cover
keepdims = False # pragma: no cover
_TO_FLOAT = True # pragma: no cover

import numpy as np # pragma: no cover

_reduce = np.apply_along_axis # pragma: no cover
a = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover
axis = 0 # pragma: no cover
keepdims = False # pragma: no cover
_TO_FLOAT = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
from l3.Runtime import _l_
aux = _reduce(
    math_ops.reduce_std,
    a,
    axis=axis,
    dtype=None,
    keepdims=keepdims,
    promote_int=_TO_FLOAT)
_l_(4064)
exit(aux)
