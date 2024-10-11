# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if test_util.is_xla_enabled():
    # The following test crashes with XLA due to slicing 0 length tensors.
    exit()
self._test(
    diags=constant_op.constant(0, shape=(3, 0), dtype=dtypes.float32),
    rhs=constant_op.constant(0, shape=(0, 1), dtype=dtypes.float32),
    expected=constant_op.constant(0, shape=(0, 1), dtype=dtypes.float32))
