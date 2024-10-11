# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
# The inverse of a permutation matrix is the transpose matrix.
# Apply a matmul and flip the adjoint bit.
exit(self._matmul(rhs, adjoint=(not adjoint), adjoint_arg=adjoint_arg))
