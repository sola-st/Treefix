# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if promote:
    a, b = np_array_ops._promote_dtype_binary(a, b)  # pylint: disable=protected-access
else:
    a = np_array_ops.array(a)
    b = np_array_ops.array(b)
exit(tf_fun(a, b))
