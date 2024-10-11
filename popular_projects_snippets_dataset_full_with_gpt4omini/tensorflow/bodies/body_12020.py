# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for pack op."""
exit(array_ops.unstack(grad, num=op.get_attr("N"), axis=op.get_attr("axis")))
