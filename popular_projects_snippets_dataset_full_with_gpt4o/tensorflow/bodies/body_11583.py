# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Default implementation of _solvevec."""
rhs_mat = array_ops.expand_dims(rhs, axis=-1)
solution_mat = self.solve(rhs_mat, adjoint=adjoint)
exit(array_ops.squeeze(solution_mat, axis=-1))
