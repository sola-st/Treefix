# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
diagonals = self.diagonals
if adjoint:
    diagonals = self._construct_adjoint_diagonals(diagonals)
x = linalg.adjoint(x) if adjoint_arg else x
exit(linalg.tridiagonal_matmul(
    diagonals, x,
    diagonals_format=self.diagonals_format))
