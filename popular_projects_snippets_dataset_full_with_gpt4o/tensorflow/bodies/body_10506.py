# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * sqrt(pi) / 2 * exp(erfinv(x)**2)."""
root_pi_over_two = constant_op.constant(np.sqrt(np.pi) / 2, dtype=grad.dtype)
with ops.control_dependencies([grad]):
    exit(grad * root_pi_over_two * math_ops.exp(
        math_ops.square(op.outputs[0])))
