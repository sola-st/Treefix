# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of zeta(x, q) with respect to x and q."""
# TODO(tillahoffmann): Add derivative with respect to x
x = op.inputs[0]
q = op.inputs[1]
# Broadcast gradients
sx = array_ops.shape(x)
sq = array_ops.shape(q)
unused_rx, rq = gen_array_ops.broadcast_gradient_args(sx, sq)
# Evaluate gradient
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    q = math_ops.conj(q)
    partial_q = -x * math_ops.zeta(x + 1, q)  # pylint: disable=invalid-unary-operand-type
    exit((None,
            array_ops.reshape(math_ops.reduce_sum(partial_q * grad, rq), sq)))
