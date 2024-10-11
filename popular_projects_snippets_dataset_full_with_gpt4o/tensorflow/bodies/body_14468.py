# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
a = np_array_ops.array(a)
v = np_array_ops.array(init_val, dtype=a.dtype)
exit(reduction(
    np_array_ops.where(isnan(a), v, a),
    axis=axis,
    dtype=dtype,
    keepdims=keepdims))
