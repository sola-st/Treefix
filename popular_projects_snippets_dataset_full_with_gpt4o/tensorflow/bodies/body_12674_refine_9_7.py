import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: cholesky(matrix @ matrix.T + l2_regularizer * np.eye(matrix.shape[0]), lower=True) # pragma: no cover
matrix = np.array([[1, 2], [3, 4]]) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': np.matmul}) # pragma: no cover
cholesky_solve = lambda chol, rhs: solve_triangular(chol, solve_triangular(chol, rhs, lower=True, trans='T')) # pragma: no cover
rhs = np.array([[5, 6], [7, 8]]) # pragma: no cover

import numpy as np # pragma: no cover

class _RegularizedGramianCholesky:# pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind):# pragma: no cover
        self.l2_regularizer = l2_regularizer# pragma: no cover
        self.first_kind = first_kind# pragma: no cover
        self.matrix = matrix# pragma: no cover
        gramian = np.dot(matrix, matrix.T) + l2_regularizer * np.eye(matrix.shape[0])# pragma: no cover
        self.chol = cholesky(gramian, lower=True)# pragma: no cover
    def solve(self, rhs):# pragma: no cover
        return cho_solve((self.chol, True), rhs) # pragma: no cover
matrix = np.array([[1, 2], [3, 4]], dtype=np.float32) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': lambda a, b, adjoint_a=False: np.matmul(a.T if adjoint_a else a, b)}) # pragma: no cover
cholesky_solve = lambda chol, rhs: chol.solve(rhs) # pragma: no cover
rhs = np.array([[1.0], [1.0]], dtype=np.float32) # pragma: no cover

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
