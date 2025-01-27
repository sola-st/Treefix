# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
dtype = dtypes.complex64
if x.dtype in [dtypes.float64, dtypes.complex128]:
    dtype = dtypes.complex128
exit(math_ops.cast(x, dtype))
