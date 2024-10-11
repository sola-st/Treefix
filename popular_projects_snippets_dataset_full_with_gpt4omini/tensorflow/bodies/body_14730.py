# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
exit((array_ops.zeros(
    array_ops.concat([a_shape[:-1], [0]], 0), dtype=a.dtype), 0))
