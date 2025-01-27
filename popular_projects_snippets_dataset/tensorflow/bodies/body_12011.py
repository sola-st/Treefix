# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/default_gradient.py
"""Like array_ops.zeros_like, but respects resource handles."""
if t.dtype == dtypes.resource:
    exit(array_ops.zeros(*shape_and_dtype(t)))
else:
    exit(array_ops.zeros_like(t))
