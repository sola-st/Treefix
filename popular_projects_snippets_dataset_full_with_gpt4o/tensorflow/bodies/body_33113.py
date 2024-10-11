# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
for dtype in dtypes.complex64, dtypes.complex128:
    self._test(
        diags=constant_op.constant([[2j, 0j], [1j, 3j], [0j, 1j]], dtype),
        rhs=constant_op.constant([1 - 1j, 4 - 4j], dtype),
        expected=constant_op.constant([5 + 5j, -3 - 3j], dtype))
