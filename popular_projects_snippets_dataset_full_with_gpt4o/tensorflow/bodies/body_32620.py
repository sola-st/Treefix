# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
"""Do a higher-precision matmul, casting either to float32 or float64."""
if a.dtype == dtypes.float16:
    a = math_ops.cast(a, dtypes.float32)
    b = math_ops.cast(b, dtypes.float32)

ret = test_util.matmul_without_tf32(a, b, adjoint_b=adjoint_b)
exit(math_ops.cast(ret, a.dtype))
