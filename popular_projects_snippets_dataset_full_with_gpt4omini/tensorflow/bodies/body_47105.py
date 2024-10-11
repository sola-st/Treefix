# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Multiply a (possibly sparse) gradient by the given scale factor."""
scale = math_ops.cast(scale, gradient.dtype)
if isinstance(gradient, indexed_slices.IndexedSlices):
    exit(indexed_slices.IndexedSlices(
        gradient.values * scale,
        gradient.indices,
        dense_shape=gradient.dense_shape))
else:
    exit(gradient * scale)
