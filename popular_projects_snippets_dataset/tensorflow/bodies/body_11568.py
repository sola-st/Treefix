# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
dense = self.to_dense()
logging.warn(
    "Using (possibly slow) default implementation of assert_self_adjoint."
    "  Requires conversion to a dense matrix.")
exit(check_ops.assert_equal(
    dense,
    linalg.adjoint(dense),
    message="Matrix was not equal to its adjoint."))
