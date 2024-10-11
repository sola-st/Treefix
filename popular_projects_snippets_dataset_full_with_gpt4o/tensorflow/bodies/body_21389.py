# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad.py
acc = self.get_slot(var, "accumulator")
exit(training_ops.resource_sparse_apply_proximal_adagrad(
    var.handle, acc.handle,
    math_ops.cast(self._learning_rate_tensor, grad.dtype),
    math_ops.cast(self._l1_regularization_strength_tensor, grad.dtype),
    math_ops.cast(self._l2_regularization_strength_tensor, grad.dtype),
    grad, indices,
    use_locking=self._use_locking))
