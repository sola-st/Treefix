# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns the gradient of x and y given the gradient of x * y."""
x = op.inputs[0]
y = op.inputs[1]
adj_x = op.get_attr("adj_x")
adj_y = op.get_attr("adj_y")

if not adj_x:
    if not adj_y:
        grad_x = math_ops.matmul(grad, y, adjoint_a=False, adjoint_b=True)
        grad_y = math_ops.matmul(x, grad, adjoint_a=True, adjoint_b=False)
    else:
        grad_x = math_ops.matmul(grad, y, adjoint_a=False, adjoint_b=False)
        grad_y = math_ops.matmul(grad, x, adjoint_a=True, adjoint_b=False)
else:
    if not adj_y:
        grad_x = math_ops.matmul(y, grad, adjoint_a=False, adjoint_b=True)
        grad_y = math_ops.matmul(x, grad, adjoint_a=False, adjoint_b=False)
    else:
        grad_x = math_ops.matmul(y, grad, adjoint_a=True, adjoint_b=True)
        grad_y = math_ops.matmul(grad, x, adjoint_a=True, adjoint_b=True)

exit((grad_x, grad_y))
