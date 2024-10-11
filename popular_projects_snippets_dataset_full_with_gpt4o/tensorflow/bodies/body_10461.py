# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for SegmentSum."""
exit((array_ops.gather(grad, op.inputs[1]), None))
