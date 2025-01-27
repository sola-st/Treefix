# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * 1/sinh(y)."""
y = op.outputs[0]
with ops.control_dependencies([grad]):
    y = math_ops.conj(y)
    exit(grad / math_ops.sinh(y))
