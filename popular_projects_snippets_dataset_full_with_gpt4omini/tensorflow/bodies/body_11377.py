# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
if self._assert_proper_shapes:
    aps = linear_operator_util.assert_compatible_matrix_dimensions(self, rhs)
    rhs = control_flow_ops.with_dependencies([aps], rhs)
exit(rhs / self._make_multiplier_matrix(conjugate=adjoint))
