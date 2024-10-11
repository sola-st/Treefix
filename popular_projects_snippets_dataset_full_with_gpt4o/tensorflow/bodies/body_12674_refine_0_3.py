import numpy as np # pragma: no cover

matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32) # pragma: no cover
l2_regularizer = 0.01 # pragma: no cover
rhs = np.array([[1.0], [0.0]], dtype=np.float32) # pragma: no cover

import numpy as np # pragma: no cover

class _RegularizedGramianCholesky:# pragma: no cover
    def __init__(self, matrix, l2_regularizer, first_kind):# pragma: no cover
        regularized_matrix = matrix @ matrix.T + l2_regularizer * np.identity(matrix.shape[0], dtype=matrix.dtype)# pragma: no cover
        self.chol = tf.linalg.cholesky(regularized_matrix)# pragma: no cover
# pragma: no cover
    def __call__(self):# pragma: no cover
        return self.chol # pragma: no cover
matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32) # pragma: no cover
l2_regularizer = 0.01 # pragma: no cover
rhs = np.array([[1.0], [0.0]], dtype=np.float32) # pragma: no cover

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
