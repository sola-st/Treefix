# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if axis is None:
    exit(concatenate([np_array_ops.ravel(arr), np_array_ops.ravel(values)], 0))
else:
    exit(concatenate([arr, values], axis=axis))
