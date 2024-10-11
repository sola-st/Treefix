# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_gradient_descent.py
exit(training_ops.sparse_apply_proximal_gradient_descent(
    var,
    self._learning_rate_tensor,
    self._l1_regularization_strength_tensor,
    self._l2_regularization_strength_tensor,
    grad.values,
    grad.indices,
    use_locking=self._use_locking).op)
