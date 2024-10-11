# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if dtype:
    dtype = np_utils.result_type(dtype)
exit(array_ops.ones(shape, dtype=dtype))
