# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of psi(n, x) with respect to n and x."""
# TODO(tillahoffmann): Add derivative with respect to n
n = op.inputs[0]
x = op.inputs[1]
# Broadcast gradients
sn = array_ops.shape(n)
sx = array_ops.shape(x)
unused_rn, rx = gen_array_ops.broadcast_gradient_args(sn, sx)
# Evaluate gradient
with ops.control_dependencies([grad]):
    n = math_ops.conj(n)
    x = math_ops.conj(x)
    partial_x = math_ops.polygamma(n + 1, x)
    exit((None,
            array_ops.reshape(math_ops.reduce_sum(partial_x * grad, rx), sx)))
