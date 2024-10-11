import numpy as np # pragma: no cover

_RegularizedGramianCholesky = type('Mock', (object,), {'__init__': lambda self, matrix, l2_regularizer, first_kind: None}) # pragma: no cover
matrix = np.random.rand(5, 3) # pragma: no cover
l2_regularizer = 0.01 # pragma: no cover
rhs = np.random.rand(5, 1) # pragma: no cover

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
