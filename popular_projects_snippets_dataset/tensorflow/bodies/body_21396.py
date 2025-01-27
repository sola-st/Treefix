# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum.py
mom = self.get_slot(var, "momentum")
exit(training_ops.resource_sparse_apply_momentum(
    var.handle, mom.handle,
    math_ops.cast(self._learning_rate_tensor, grad.dtype),
    grad, indices,
    math_ops.cast(self._momentum_tensor, grad.dtype),
    use_locking=self._use_locking,
    use_nesterov=self._use_nesterov))
