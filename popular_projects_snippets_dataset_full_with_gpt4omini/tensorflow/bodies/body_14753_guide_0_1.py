axis = 0 # pragma: no cover
keepdims = False # pragma: no cover
def _reduce(func, inputs, axis=None, dtype=None, keepdims=False, promote_int=None): return func(inputs, axis=axis, dtype=dtype, keepdims=keepdims) # pragma: no cover

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
