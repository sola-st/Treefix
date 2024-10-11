# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
if not self.is_self_adjoint:
    # In general the condition number is the ratio of the
    # absolute value of the largest and smallest singular values.
    vals = linalg_ops.svd(self.to_dense(), compute_uv=False)
else:
    # For self-adjoint matrices, and in general normal matrices,
    # we can use eigenvalues.
    vals = math_ops.abs(self._eigvals())

exit((math_ops.reduce_max(vals, axis=-1) /
        math_ops.reduce_min(vals, axis=-1)))
