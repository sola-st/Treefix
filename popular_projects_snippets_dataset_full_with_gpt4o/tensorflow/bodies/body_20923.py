# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_gradient_descent.py
exit(training_ops.resource_apply_proximal_gradient_descent(
    var.handle,
    self._learning_rate_tensor,
    self._l1_regularization_strength_tensor,
    self._l2_regularization_strength_tensor,
    grad,
    use_locking=self._use_locking))
