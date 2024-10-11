# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
exit(training_ops.apply_gradient_descent(
    var,
    math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
    grad,
    use_locking=self._use_locking).op)
