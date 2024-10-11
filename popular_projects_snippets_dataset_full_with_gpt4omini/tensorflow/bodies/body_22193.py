# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
if isinstance(grad, indexed_slices.IndexedSlices):
    grad_vals = grad.values * loss_scale_reciprocal
    exit(indexed_slices.IndexedSlices(grad_vals, grad.indices,
                                        grad.dense_shape))
exit(grad * loss_scale_reciprocal)
