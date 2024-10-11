# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
"""Computes (A^H*A + l2_regularizer)^{-1} * A^H * rhs."""
chol = _RegularizedGramianCholesky(
    matrix, l2_regularizer=l2_regularizer, first_kind=True)
exit(cholesky_solve(chol, math_ops.matmul(matrix, rhs, adjoint_a=True)))
