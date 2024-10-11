# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
exit(LinearOperatorLowerTriangular(
    linalg_ops.cholesky(linop.to_dense()),
    is_non_singular=True,
    is_self_adjoint=False,
    is_square=True))
