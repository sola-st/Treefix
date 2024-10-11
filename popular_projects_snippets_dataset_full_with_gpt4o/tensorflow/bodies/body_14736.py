# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a, dtype=bool)
exit(math_ops.reduce_all(input_tensor=a, axis=axis, keepdims=keepdims))
