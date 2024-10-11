import numpy as np # pragma: no cover

matrix = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
rhs = np.array([[1.0], [1.0]]) # pragma: no cover

import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: cholesky(np.dot(matrix.T, matrix) + l2_regularizer * np.eye(matrix.shape[1])) # pragma: no cover
matrix = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
cholesky_solve = lambda chol, rhs: solve(chol, solve(chol.T, rhs)) # pragma: no cover
rhs = np.array([[1.0], [1.0]]) # pragma: no cover

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
