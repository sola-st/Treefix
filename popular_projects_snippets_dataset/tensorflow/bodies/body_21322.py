# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
exit(training_ops.resource_apply_gradient_descent(
    handle.handle, math_ops.cast(self._learning_rate_tensor,
                                 grad.dtype.base_dtype),
    grad, use_locking=self._use_locking))
