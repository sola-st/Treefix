# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
if self.base_operator.is_non_singular is False:
    raise ValueError(
        "Solve not implemented unless this is a perturbation of a "
        "non-singular LinearOperator.")
# The Woodbury formula gives:
# https://en.wikipedia.org/wiki/Woodbury_matrix_identity
#   (L + UDV^H)^{-1}
#   = L^{-1} - L^{-1} U (D^{-1} + V^H L^{-1} U)^{-1} V^H L^{-1}
#   = L^{-1} - L^{-1} U C^{-1} V^H L^{-1}
# where C is the capacitance matrix, C := D^{-1} + V^H L^{-1} U
# Note also that, with ^{-H} being the inverse of the adjoint,
#   (L + UDV^H)^{-H}
#   = L^{-H} - L^{-H} V C^{-H} U^H L^{-H}
l = self.base_operator
if adjoint:
    # If adjoint, U and V have flipped roles in the operator.
    v, u = self._get_uv_as_tensors()
    # Capacitance should still be computed with u=self.u and v=self.v, which
    # after the "flip" on the line above means u=v, v=u. I.e. no need to
    # "flip" in the capacitance call, since the call to
    # matrix_solve_with_broadcast below is done with the `adjoint` argument,
    # and this takes care of things.
    capacitance = self._make_capacitance(u=v, v=u)
else:
    u, v = self._get_uv_as_tensors()
    capacitance = self._make_capacitance(u=u, v=v)

# L^{-1} rhs
linv_rhs = l.solve(rhs, adjoint=adjoint, adjoint_arg=adjoint_arg)
# V^H L^{-1} rhs
vh_linv_rhs = math_ops.matmul(v, linv_rhs, adjoint_a=True)
# C^{-1} V^H L^{-1} rhs
if self._use_cholesky:
    capinv_vh_linv_rhs = linalg_ops.cholesky_solve(
        linalg_ops.cholesky(capacitance), vh_linv_rhs)
else:
    capinv_vh_linv_rhs = linear_operator_util.matrix_solve_with_broadcast(
        capacitance, vh_linv_rhs, adjoint=adjoint)
# U C^{-1} V^H M^{-1} rhs
u_capinv_vh_linv_rhs = math_ops.matmul(u, capinv_vh_linv_rhs)
# L^{-1} U C^{-1} V^H L^{-1} rhs
linv_u_capinv_vh_linv_rhs = l.solve(u_capinv_vh_linv_rhs, adjoint=adjoint)

# L^{-1} - L^{-1} U C^{-1} V^H L^{-1}
exit(linv_rhs - linv_u_capinv_vh_linv_rhs)
