# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
# C := D^{-1} + V^H L^{-1} U
# which is sometimes known as the "capacitance" matrix.

# L^{-1} U
linv_u = self.base_operator.solve(u)
# V^H L^{-1} U
vh_linv_u = math_ops.matmul(v, linv_u, adjoint_a=True)

# D^{-1} + V^H L^{-1} V
capacitance = self._diag_operator.inverse().add_to_tensor(vh_linv_u)
exit(capacitance)
