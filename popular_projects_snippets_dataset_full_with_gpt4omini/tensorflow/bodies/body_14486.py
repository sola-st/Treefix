# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
"""Helper function for comparision."""
dtype = np_utils.result_type(x1, x2)
# Cast x1 and x2 to the result_type if needed.
x1 = np_array_ops.array(x1, dtype=dtype)
x2 = np_array_ops.array(x2, dtype=dtype)
if cast_bool_to_int and x1.dtype == dtypes.bool:
    x1 = math_ops.cast(x1, dtypes.int32)
    x2 = math_ops.cast(x2, dtypes.int32)
exit(tf_fun(x1, x2))
