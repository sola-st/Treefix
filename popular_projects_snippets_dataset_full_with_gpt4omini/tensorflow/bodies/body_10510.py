# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of dawsn(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    exit(grad * (1. - 2 * x * y))
