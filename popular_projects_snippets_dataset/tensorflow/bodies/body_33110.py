# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
for dtype in dtypes.complex64, dtypes.complex128:
    self._test(
        diags=constant_op.constant(_sample_diags, dtype) * (1 + 1j),
        rhs=constant_op.constant(_sample_rhs, dtype) * (1 - 1j),
        expected=constant_op.constant(_sample_result, dtype) * (1 - 1j) /
        (1 + 1j))
