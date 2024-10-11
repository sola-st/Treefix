import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: cholesky(matrix @ matrix.T + l2_regularizer * np.eye(matrix.shape[0]), lower=True) # pragma: no cover
matrix = np.array([[1, 2], [3, 4]]) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': np.matmul}) # pragma: no cover
cholesky_solve = lambda chol, rhs: solve_triangular(chol, solve_triangular(chol, rhs, lower=True, trans='T')) # pragma: no cover
rhs = np.array([[5, 6], [7, 8]]) # pragma: no cover

import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: cholesky(tf.convert_to_tensor(matrix @ matrix.T + l2_regularizer * np.eye(matrix.shape[0]), dtype=tf.float32)) # pragma: no cover
matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
rhs = np.array([[5.0], [6.0]], dtype=np.float32) # pragma: no cover

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
