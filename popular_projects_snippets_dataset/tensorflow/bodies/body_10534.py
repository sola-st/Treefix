# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns 0."""
x = op.inputs[0]
exit(array_ops.zeros_like(x))
