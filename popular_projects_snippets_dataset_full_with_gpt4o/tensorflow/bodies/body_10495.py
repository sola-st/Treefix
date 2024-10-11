# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of xlog1py(x, y) with respect to x and y."""
x = op.inputs[0]
y = op.inputs[1]
sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
with ops.control_dependencies([grad]):
    not_zero_x = math_ops.cast(
        math_ops.not_equal(x, math_ops.cast(0., dtype=x.dtype)), dtype=x.dtype)
    partial_x = gen_math_ops.xlog1py(not_zero_x, y)
    partial_y = gen_math_ops.xdivy(x, y + 1.)
    exit((array_ops.reshape(math_ops.reduce_sum(partial_x * grad, rx), sx),
            array_ops.reshape(math_ops.reduce_sum(partial_y * grad, ry), sy)))
