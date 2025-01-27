# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of nextafter(x1, x2) with respect to x1 and x2."""
x1 = op.inputs[0]
x2 = op.inputs[1]
s_x1 = array_ops.shape(x1)
s_x2 = array_ops.shape(x2)
r_x1, r_x2 = gen_array_ops.broadcast_gradient_args(s_x1, s_x2)
with ops.control_dependencies([grad]):
    partial_x1 = array_ops.ones(s_x1, dtype=x1.dtype)
    partial_x2 = array_ops.zeros(s_x2, dtype=x2.dtype)
    exit((array_ops.reshape(
        math_ops.reduce_sum(partial_x1 * grad, r_x1), s_x1),
            array_ops.reshape(
                math_ops.reduce_sum(partial_x2 * grad, r_x2), s_x2)))
