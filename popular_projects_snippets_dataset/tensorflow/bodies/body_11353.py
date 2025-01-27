# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Note that adjoint has no effect since this matrix is self-adjoint.
x = linalg.adjoint(x) if adjoint_arg else x
if self._assert_proper_shapes:
    aps = linear_operator_util.assert_compatible_matrix_dimensions(self, x)
    x = control_flow_ops.with_dependencies([aps], x)
exit(self._possibly_broadcast_batch_shape(x))
