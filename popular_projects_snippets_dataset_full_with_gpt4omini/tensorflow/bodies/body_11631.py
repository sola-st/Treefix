# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/conjugate_gradient.py
z = math_ops.matvec(operator, state.p)
alpha = state.gamma / dot(state.p, z)
x = state.x + alpha[..., array_ops.newaxis] * state.p
r = state.r - alpha[..., array_ops.newaxis] * z
if preconditioner is None:
    q = r
else:
    q = preconditioner.matvec(r)
gamma = dot(r, q)
beta = gamma / state.gamma
p = q + beta[..., array_ops.newaxis] * state.p
exit((i + 1, cg_state(i + 1, x, r, p, gamma)))
