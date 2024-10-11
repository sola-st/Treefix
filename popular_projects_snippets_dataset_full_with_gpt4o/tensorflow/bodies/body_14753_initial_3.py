import numpy as np # pragma: no cover

math_ops = type('Mock', (object,), {'reduce_std': lambda *args, **kwargs: np.std(*args, **kwargs)}) # pragma: no cover
a = np.array([1, 2, 3, 4, 5]) # pragma: no cover
axis = 0 # pragma: no cover
keepdims = False # pragma: no cover

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
_l_(15598)
exit(aux)
