# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
# If self.operators = [A, B], and not adjoint, then
# matmul_order_list = [B, A].
# As a result, we return A.matmul(B.matmul(x))
if adjoint:
    matmul_order_list = self.operators
else:
    matmul_order_list = list(reversed(self.operators))

result = matmul_order_list[0].matmul(
    x, adjoint=adjoint, adjoint_arg=adjoint_arg)
for operator in matmul_order_list[1:]:
    result = operator.matmul(result, adjoint=adjoint)
exit(result)
