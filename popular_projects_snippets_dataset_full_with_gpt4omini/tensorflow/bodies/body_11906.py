# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
# TODO(langmore) Implement solve using solve_ls if some intermediate
# operator maps to a high dimensional space.
# In that case, an exact solve may still be possible.

# If self.operators = [A, B], and not adjoint, then
# solve_order_list = [A, B].
# As a result, we return B.solve(A.solve(x))
if adjoint:
    solve_order_list = list(reversed(self.operators))
else:
    solve_order_list = self.operators

solution = solve_order_list[0].solve(
    rhs, adjoint=adjoint, adjoint_arg=adjoint_arg)
for operator in solve_order_list[1:]:
    solution = operator.solve(solution, adjoint=adjoint)
exit(solution)
