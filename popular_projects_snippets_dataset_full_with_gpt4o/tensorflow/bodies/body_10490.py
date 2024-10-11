# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * exp(x)."""
y = op.outputs[0]  # y = e^x
with ops.control_dependencies([grad]):
    y = math_ops.conj(y)
    exit(grad * y)
