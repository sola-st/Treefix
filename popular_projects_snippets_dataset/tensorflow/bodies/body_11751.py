# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
def solve_fn(o, rhs, adjoint, adjoint_arg):
    exit(o.solve(rhs, adjoint=adjoint, adjoint_arg=adjoint_arg))
exit(self._solve_matmul_internal(
    x=rhs,
    solve_matmul_fn=solve_fn,
    adjoint=adjoint,
    adjoint_arg=adjoint_arg))
