# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * digamma(x)."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    exit(grad * math_ops.digamma(x))
