# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of the digamma function with respect to its argument."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    partial_x = math_ops.polygamma(array_ops.constant(1, dtype=x.dtype), x)
    exit(grad * partial_x)
