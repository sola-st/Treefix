# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
a, b = np_array_ops._promote_dtype(a, b)  # pylint: disable=protected-access
a = np_array_ops.reshape(a, [-1])
b = np_array_ops.reshape(b, [-1])
if a.dtype == np_dtypes.complex128 or a.dtype == np_dtypes.complex64:
    a = conj(a)
exit(dot(a, b))
