import numpy as np # pragma: no cover
from functools import reduce as _reduce # pragma: no cover

a = np.random.rand(10, 10) # pragma: no cover

import numpy as np # pragma: no cover

_reduce = lambda func, iterable, **kwargs: np.array([func(iterable, **kwargs)]) # pragma: no cover
class MathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def reduce_std(a, axis=None, dtype=None, keepdims=False): # pragma: no cover
        return np.std(a, axis=axis, dtype=dtype, keepdims=keepdims) # pragma: no cover
math_ops = MathOps() # pragma: no cover
a = np.array([[1, 2, 3], [4, 5, 6]]) # pragma: no cover
axis = 0 # pragma: no cover
keepdims = True # pragma: no cover
_TO_FLOAT = np.float32 # pragma: no cover

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
