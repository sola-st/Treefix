import numpy as np # pragma: no cover

matrix = np.array([[1, 2], [3, 4]], dtype=np.float32) # pragma: no cover
l2_regularizer = np.array([[0.1, 0], [0, 0.1]], dtype=np.float32) # pragma: no cover
rhs = np.array([[5], [6]], dtype=np.float32) # pragma: no cover

import numpy as np # pragma: no cover

class _RegularizedGramianCholesky:# pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind=False):# pragma: no cover
        self.matrix = matrix# pragma: no cover
        self.l2_regularizer = l2_regularizer# pragma: no cover
        self.first_kind = first_kind# pragma: no cover
        regularized_matrix = matrix @ matrix.T + l2_regularizer * tf.eye(matrix.shape[0])# pragma: no cover
        self.cholesky_factor = tf.linalg.cholesky(regularized_matrix)# pragma: no cover
    def __call__(self):# pragma: no cover
        return self.cholesky_factor # pragma: no cover

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
