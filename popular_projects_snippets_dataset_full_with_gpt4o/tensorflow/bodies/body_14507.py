# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if axis is None:
    a = array_ops.reshape(a, [-1])
    axis = 0

exit(sort_ops.argsort(a, axis, stable=stable))
