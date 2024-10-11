# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
matrix = self._makeTridiagonalMatrix(diags[..., 0, :-1], diags[..., 1, :],
                                     diags[..., 2, 1:])
exit(math_ops.matmul(matrix, rhs))
