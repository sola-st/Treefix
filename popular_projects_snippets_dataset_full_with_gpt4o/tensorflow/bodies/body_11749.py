# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
def matmul_fn(o, x, adjoint, adjoint_arg):
    exit(o.matmul(x, adjoint=adjoint, adjoint_arg=adjoint_arg))
exit(self._solve_matmul_internal(
    x=x,
    solve_matmul_fn=matmul_fn,
    adjoint=adjoint,
    adjoint_arg=adjoint_arg))
