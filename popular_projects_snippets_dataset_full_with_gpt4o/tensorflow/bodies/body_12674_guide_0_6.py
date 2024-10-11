import numpy as np # pragma: no cover

class _RegularizedGramianCholesky: # pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind): # pragma: no cover
        I = np.eye(matrix.shape[1]) # pragma: no cover
        self.chol = cholesky(np.dot(matrix.T, matrix) + l2_regularizer * I) # pragma: no cover
    def solve(self, rhs): # pragma: no cover
        return solve_triangular(self.chol, solve_triangular(self.chol, rhs.T, lower=True).T, lower=True) # pragma: no cover
 # pragma: no cover
def cholesky_solve(chol, rhs): # pragma: no cover
    return chol.solve(rhs) # pragma: no cover
 # pragma: no cover
matrix = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover
rhs = np.array([[1.0], [1.0]]) # pragma: no cover
l2_regularizer = 0.01 # pragma: no cover

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
