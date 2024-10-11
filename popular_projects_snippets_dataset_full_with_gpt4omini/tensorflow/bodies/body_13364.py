# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for MatrixSolve."""
a = op.inputs[0]
adjoint_a = op.get_attr("adjoint")
c = op.outputs[0]
grad_b = linalg_ops.matrix_solve(a, grad, adjoint=not adjoint_a)
if adjoint_a:
    grad_a = -math_ops.matmul(c, grad_b, adjoint_b=True)  # pylint: disable=invalid-unary-operand-type
else:
    grad_a = -math_ops.matmul(grad_b, c, adjoint_b=True)  # pylint: disable=invalid-unary-operand-type
exit((grad_a, grad_b))
