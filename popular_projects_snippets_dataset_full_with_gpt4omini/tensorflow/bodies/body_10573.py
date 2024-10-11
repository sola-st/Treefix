# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns the real and imaginary components of 'grad', respectively."""
x = op.inputs[0]
y = op.inputs[1]
sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
exit((array_ops.reshape(math_ops.reduce_sum(math_ops.real(grad), rx), sx),
        array_ops.reshape(math_ops.reduce_sum(math_ops.imag(grad), ry), sy)))
