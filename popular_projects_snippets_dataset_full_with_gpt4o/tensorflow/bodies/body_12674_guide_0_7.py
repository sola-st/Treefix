import numpy as np # pragma: no cover

class _RegularizedGramianCholesky:# pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind):# pragma: no cover
        self.matrix = matrix# pragma: no cover
        self.l2_regularizer = l2_regularizer# pragma: no cover
        self.chol = np.linalg.cholesky(matrix @ matrix.T + np.eye(matrix.shape[0]) * l2_regularizer)# pragma: no cover
# pragma: no cover
    def solve(self, rhs):# pragma: no cover
        return np.linalg.solve(self.chol.T, np.linalg.solve(self.chol, rhs))# pragma: no cover
# pragma: no cover
def cholesky_solve(chol, rhs):# pragma: no cover
    return chol.solve(rhs) # pragma: no cover
matrix = np.array([[1, 2], [3, 4]], dtype=float) # pragma: no cover
l2_regularizer = 0.01 # pragma: no cover
rhs = np.array([[1], [0]], dtype=float) # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': lambda a, b, adjoint_a=False: a.T @ b if adjoint_a else a @ b}) # pragma: no cover

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
