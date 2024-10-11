# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
delta = indexed_slices.IndexedSlices(
    grad.values *
    math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
    grad.indices, grad.dense_shape)
exit(var.scatter_sub(delta, use_locking=self._use_locking))
