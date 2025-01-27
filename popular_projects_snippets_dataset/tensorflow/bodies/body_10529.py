# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of betainc(a, b, x) with respect to x."""
# TODO(ebrevdo): Perhaps add the derivative w.r.t. a, b
a, b, x = op.inputs

# two cases: x is a scalar and a/b are same-shaped tensors, or vice
# versa; so its sufficient to check against shape(a).
sa = array_ops.shape(a)
sx = array_ops.shape(x)
_, rx = gen_array_ops.broadcast_gradient_args(sa, sx)

# Perform operations in log space before summing, because terms
# can grow large.
log_beta = (
    gen_math_ops.lgamma(a) + gen_math_ops.lgamma(b) -
    gen_math_ops.lgamma(a + b))
# We use xlog1py and xlogy since the derivatives should tend to
# zero one of the tails when a is 1. or b is 1.
partial_x = math_ops.exp(math_ops.xlog1py(b - 1, -x) +
                         math_ops.xlogy(a - 1, x) - log_beta)

exit((None,  # da
    None,  # db
    array_ops.reshape(math_ops.reduce_sum(partial_x * grad, rx), sx)))
