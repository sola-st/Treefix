# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
dtype = np_utils.result_type_unary(a, dtype)

dtype = dtypes.as_dtype(dtype)  # Work around b/149877262
exit(array_ops.zeros_like(a, dtype))
