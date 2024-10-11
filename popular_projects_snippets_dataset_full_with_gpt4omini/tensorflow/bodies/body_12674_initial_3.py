import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: np.linalg.cholesky(np.dot(matrix, matrix.T) + l2_regularizer * np.eye(matrix.shape[0])) # pragma: no cover
matrix = np.random.rand(3, 2) # pragma: no cover
l2_regularizer = 0.1 # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': staticmethod(lambda a, b, adjoint_a=False: np.matmul(a.conj().T if adjoint_a else a, b))}) # pragma: no cover
cholesky_solve = lambda chol, rhs: np.linalg.solve(chol, rhs) # pragma: no cover
rhs = np.random.rand(3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
from l3.Runtime import _l_
"""Computes A^H * (A*A^H + l2_regularizer)^{-1} * rhs."""
chol = _RegularizedGramianCholesky(
    matrix, l2_regularizer=l2_regularizer, first_kind=False)
_l_(8671)
aux = math_ops.matmul(matrix, cholesky_solve(chol, rhs), adjoint_a=True)
_l_(8672)
exit(aux)
