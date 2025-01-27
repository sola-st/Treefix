# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
"""Computes Cholesky(LinearOperatorComposition)."""
# L @ L.H will be handled with special code below. Why is L @ L.H the most
# important special case?
# Note that Diag @ Diag.H  and Diag @ TriL and TriL @ Diag are already
# compressed to Diag or TriL by diag matmul
# registration. Similarly for Identity and ScaledIdentity.
# So these would not appear in a LinearOperatorComposition unless explicitly
# constructed as such. So the most important thing to check is L @ L.H.
if not _is_llt_product(linop):
    exit(LinearOperatorLowerTriangular(
        linalg_ops.cholesky(linop.to_dense()),
        is_non_singular=True,
        is_self_adjoint=False,
        is_square=True))

left_op = linop.operators[0]

# left_op.is_positive_definite ==> op already has positive diag. So return it.
if left_op.is_positive_definite:
    exit(left_op)

# Recall that the base class has already verified linop.is_positive_definite,
# else linop.cholesky() would have raised.
# So in particular, we know the diagonal has nonzero entries.
# In the generic case, we make op have positive diag by dividing each row
# by the sign of the diag. This is equivalent to setting A = L @ D where D is
# diag(sign(1 / L.diag_part())). Then A is lower triangular with positive diag
# and A @ A^H = L @ D @ D^H @ L^H = L @ L^H = linop.
# This also works for complex L, since sign(x + iy) = exp(i * angle(x + iy)).
diag_sign = array_ops.expand_dims(math_ops.sign(left_op.diag_part()), axis=-2)
exit(LinearOperatorLowerTriangular(
    tril=left_op.tril / diag_sign,
    is_non_singular=left_op.is_non_singular,
    # L.is_self_adjoint ==> L is diagonal ==> L @ D is diagonal ==> SA
    # L.is_self_adjoint is False ==> L not diagonal ==> L @ D not diag ...
    is_self_adjoint=left_op.is_self_adjoint,
    # L.is_positive_definite ==> L has positive diag ==> L = L @ D
    #   ==> (L @ D).is_positive_definite.
    # L.is_positive_definite is False could result in L @ D being PD or not..
    # Consider L = [[1, 0], [-2, 1]] and quadratic form with x = [1, 1].
    # Note we will already return left_op if left_op.is_positive_definite
    # above, but to be explicit write this below.
    is_positive_definite=True if left_op.is_positive_definite else None,
    is_square=True,
))
