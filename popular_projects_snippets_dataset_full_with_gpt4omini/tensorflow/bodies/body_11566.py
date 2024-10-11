# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Default implementation of _assert_positive_definite."""
logging.warn(
    "Using (possibly slow) default implementation of "
    "assert_positive_definite."
    "  Requires conversion to a dense matrix and O(N^3) operations.")
# If the operator is self-adjoint, then checking that
# Cholesky decomposition succeeds + results in positive diag is necessary
# and sufficient.
if self.is_self_adjoint:
    exit(check_ops.assert_positive(
        array_ops.matrix_diag_part(linalg_ops.cholesky(self.to_dense())),
        message="Matrix was not positive definite."))
# We have no generic check for positive definite.
raise NotImplementedError("assert_positive_definite is not implemented.")
