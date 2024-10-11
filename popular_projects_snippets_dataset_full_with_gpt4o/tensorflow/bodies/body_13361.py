# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Equiv to matmul(x, adjoint(matrix_inverse(r))) if r is upper-tri."""
exit(_linalg.adjoint(
    linalg_ops.matrix_triangular_solve(
        r, _linalg.adjoint(x), lower=False, adjoint=False)))
