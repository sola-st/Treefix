# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * exp(x)."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    y = math_ops.exp(x)
    exit(grad * y)
