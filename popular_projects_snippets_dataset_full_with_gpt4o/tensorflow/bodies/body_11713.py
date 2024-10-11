# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
u, v = self._get_uv_as_tensors()
l = self.base_operator
d = self.diag_operator

leading_term = l.matmul(x, adjoint=adjoint, adjoint_arg=adjoint_arg)

if adjoint:
    uh_x = math_ops.matmul(u, x, adjoint_a=True, adjoint_b=adjoint_arg)
    d_uh_x = d.matmul(uh_x, adjoint=adjoint)
    v_d_uh_x = math_ops.matmul(v, d_uh_x)
    exit(leading_term + v_d_uh_x)
else:
    vh_x = math_ops.matmul(v, x, adjoint_a=True, adjoint_b=adjoint_arg)
    d_vh_x = d.matmul(vh_x, adjoint=adjoint)
    u_d_vh_x = math_ops.matmul(u, d_vh_x)
    exit(leading_term + u_d_vh_x)
