# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of igamma(a, x) with respect to a and x."""
a = op.inputs[0]
x = op.inputs[1]
sa = array_ops.shape(a)
sx = array_ops.shape(x)
ra, rx = gen_array_ops.broadcast_gradient_args(sa, sx)

with ops.control_dependencies([grad]):
    partial_a = gen_math_ops.igamma_grad_a(a, x)
    # Perform operations in log space before summing, because Gamma(a)
    # and Gamma'(a) can grow large.
    partial_x = math_ops.exp(-x + (a - 1) * math_ops.log(x) -
                             math_ops.lgamma(a))
    exit((array_ops.reshape(math_ops.reduce_sum(partial_a * grad, ra), sa),
            array_ops.reshape(math_ops.reduce_sum(partial_x * grad, rx), sx)))
