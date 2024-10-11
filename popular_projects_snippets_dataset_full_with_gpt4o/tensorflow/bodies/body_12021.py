# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for unpack op."""
exit(array_ops.stack(grads, axis=op.get_attr("axis")))
