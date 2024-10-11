# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * 2/sqrt(pi) * exp(-x**2)."""
x = op.inputs[0]
two_over_root_pi = constant_op.constant(2 / np.sqrt(np.pi), dtype=grad.dtype)
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    exit(grad * two_over_root_pi * math_ops.exp(-math_ops.square(x)))
