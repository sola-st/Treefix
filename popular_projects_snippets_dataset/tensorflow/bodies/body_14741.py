# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a, dtype=dtype)

if dtype is None:
    a = _maybe_promote_to_int(a)

# If axis is None, the input is flattened.
if axis is None:
    a = ravel(a)
    axis = 0
elif axis < 0:
    axis += array_ops.rank(a)
exit(math_ops.cumprod(a, axis))
