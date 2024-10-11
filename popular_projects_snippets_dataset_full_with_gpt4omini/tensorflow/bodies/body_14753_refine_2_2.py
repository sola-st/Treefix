import numpy as np # pragma: no cover
from functools import reduce as _reduce # pragma: no cover

a = np.random.rand(10, 10) # pragma: no cover

import numpy as np # pragma: no cover

a = np.array([[1, 2, 3], [4, 5, 6]]) # pragma: no cover
axis = 0 # pragma: no cover
keepdims = True # pragma: no cover

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
