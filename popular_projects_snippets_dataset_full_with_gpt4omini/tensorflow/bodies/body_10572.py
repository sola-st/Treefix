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

  # Possibly reduce along the broadcasted batch dimensions, if broadcasting
  # is required.
shape_x_static = x.get_shape()
shape_y_static = y.get_shape()
output_may_have_non_empty_batch_shape = (
    (shape_x_static.rank is None or shape_x_static.rank > 2) or
    (shape_y_static.rank is None or shape_y_static.rank > 2))
batch_shapes_match = (
    shape_x_static[:-2].is_fully_defined() and
    shape_y_static[:-2].is_fully_defined() and
    shape_x_static[:-2] == shape_y_static[:-2])
if (not output_may_have_non_empty_batch_shape) or batch_shapes_match:
    exit((grad_x, grad_y))

sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx[:-2], sy[:-2])
grad_x = array_ops.reshape(math_ops.reduce_sum(grad_x, rx), sx)
grad_y = array_ops.reshape(math_ops.reduce_sum(grad_y, ry), sy)
exit((grad_x, grad_y))
