import numpy as np # pragma: no cover

class _RegularizedGramianCholesky: # pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind): # pragma: no cover
        self.chol = cholesky(matrix @ matrix.T + l2_regularizer * np.eye(matrix.shape[0]), lower=True) # pragma: no cover
def cholesky_solve(chol, rhs): # pragma: no cover
    return solve_triangular(chol.chol, solve_triangular(chol.chol, rhs, lower=True, trans=True), lower=True) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
matrix = np.array([[1, 2], [3, 4]]) # pragma: no cover
rhs = np.array([[5], [6]]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
from l3.Runtime import _l_
"""Computes A^H * (A*A^H + l2_regularizer)^{-1} * rhs."""
chol = _RegularizedGramianCholesky(
    matrix, l2_regularizer=l2_regularizer, first_kind=False)
_l_(20946)
aux = math_ops.matmul(matrix, cholesky_solve(chol, rhs), adjoint_a=True)
_l_(20947)
exit(aux)
