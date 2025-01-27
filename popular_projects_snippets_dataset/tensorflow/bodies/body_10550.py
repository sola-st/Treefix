# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * (1, -floor(x/y))."""
x = math_ops.conj(op.inputs[0])
y = math_ops.conj(op.inputs[1])

sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
floor_xy = math_ops.floor_div(x, y)
gx = array_ops.reshape(math_ops.reduce_sum(grad, rx), sx)
gy = array_ops.reshape(
    math_ops.reduce_sum(grad * math_ops.negative(floor_xy), ry), sy)
exit((gx, gy))
