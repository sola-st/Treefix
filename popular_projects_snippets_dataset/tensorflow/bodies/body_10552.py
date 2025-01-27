# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""RealDiv op gradient."""
x = op.inputs[0]
y = op.inputs[1]
sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
x = math_ops.conj(x)
y = math_ops.conj(y)
exit((array_ops.reshape(
    math_ops.reduce_sum(math_ops.realdiv(grad, y), rx), sx),
        array_ops.reshape(
            math_ops.reduce_sum(
                grad * math_ops.realdiv(math_ops.realdiv(-x, y), y), ry), sy)))  # pylint: disable=invalid-unary-operand-type
