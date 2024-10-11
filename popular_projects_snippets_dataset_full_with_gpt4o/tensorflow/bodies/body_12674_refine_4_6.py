import numpy as np # pragma: no cover

matrix = np.array([[1, 2], [3, 4]], dtype=np.float32) # pragma: no cover
l2_regularizer = np.array([[0.1, 0], [0, 0.1]], dtype=np.float32) # pragma: no cover
rhs = np.array([[5], [6]], dtype=np.float32) # pragma: no cover

import numpy as np # pragma: no cover

_RegularizedGramianCholesky = lambda matrix, l2_regularizer, first_kind: tf.linalg.cholesky(matrix @ tf.transpose(matrix) + l2_regularizer * tf.eye(tf.shape(matrix)[0])) # pragma: no cover

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
