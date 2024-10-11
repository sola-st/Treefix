# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
for dtype in dtypes.float32, dtypes.float64:
    self._test(
        diags=constant_op.constant(_sample_diags, dtype),
        rhs=constant_op.constant(_sample_rhs, dtype),
        expected=constant_op.constant(_sample_result, dtype))
