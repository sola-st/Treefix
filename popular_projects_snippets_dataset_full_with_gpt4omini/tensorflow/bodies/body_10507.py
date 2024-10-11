# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * sqrt(2 * pi) * exp(ndtri(x)**2 / 2)."""
root_two_pi = constant_op.constant(np.sqrt(2 * np.pi), dtype=grad.dtype)
with ops.control_dependencies([grad]):
    exit(grad * root_two_pi * math_ops.exp(
        math_ops.square(op.outputs[0]) / 2.))
