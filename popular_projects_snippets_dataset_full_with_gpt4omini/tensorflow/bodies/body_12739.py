# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
# Let:
#   y = tf.nn.softplus(x)
#   dx = gen_nn_ops.softplus_grad(dy, x) = dy / (1 + exp(-x))
# This op computes (ddy, d2x) from op.inputs == [dy, x] and grad == ddx.
dy, x = op.inputs
with ops.control_dependencies([grad]):
    ddy = gen_nn_ops.softplus_grad(grad, x)
    d2x = grad * dy / (math_ops.exp(-x) + 2.0 + math_ops.exp(x))
    exit((ddy, d2x))
