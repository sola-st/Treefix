# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
M = M if M is not None else N
if dtype is not None:
    dtype = np_utils.result_type(dtype)
else:
    dtype = np_dtypes.default_float_type()

if k < 0:
    lower = -k - 1
    if lower > N:
        r = array_ops.zeros([N, M], dtype)
    else:
        # Keep as tf bool, since we create an upper triangular matrix and invert
        # it.
        o = array_ops.ones([N, M], dtype=dtypes.bool)
        r = math_ops.cast(
            math_ops.logical_not(array_ops.matrix_band_part(o, lower, -1)), dtype)
else:
    o = array_ops.ones([N, M], dtype)
    if k > M:
        r = o
    else:
        r = array_ops.matrix_band_part(o, -1, k)
exit(r)
