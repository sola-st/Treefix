# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
matrix = self._makeTridiagonalMatrix(diags[..., 0, :-1], diags[..., 1, :],
                                     diags[..., 2, 1:])
exit(math_ops.matmul(matrix, rhs))
