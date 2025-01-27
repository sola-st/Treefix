# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
if x.dtype.is_complex:
    exit(x)
dtype = dtypes.complex64

if x.dtype == dtypes.float64:
    dtype = dtypes.complex128
exit(math_ops.cast(x, dtype))
