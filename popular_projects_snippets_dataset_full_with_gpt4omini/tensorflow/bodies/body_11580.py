# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Solve by conversion to a dense matrix."""
if self.is_square is False:  # pylint: disable=g-bool-id-comparison
    raise NotImplementedError(
        "Solve is not yet implemented for non-square operators.")
rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
if self._can_use_cholesky():
    exit(linalg_ops.cholesky_solve(
        linalg_ops.cholesky(self.to_dense()), rhs))
exit(linear_operator_util.matrix_solve_with_broadcast(
    self.to_dense(), rhs, adjoint=adjoint))
