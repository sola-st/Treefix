# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop.py
rms = self.get_slot(var, "rms")
mom = self.get_slot(var, "momentum")
if self._centered:
    mg = self.get_slot(var, "mg")
    exit(training_ops.resource_sparse_apply_centered_rms_prop(
        var.handle,
        mg.handle,
        rms.handle,
        mom.handle,
        math_ops.cast(self._learning_rate_tensor, grad.dtype),
        math_ops.cast(self._decay_tensor, grad.dtype),
        math_ops.cast(self._momentum_tensor, grad.dtype),
        math_ops.cast(self._epsilon_tensor, grad.dtype),
        grad,
        indices,
        use_locking=self._use_locking))
else:
    exit(training_ops.resource_sparse_apply_rms_prop(
        var.handle,
        rms.handle,
        mom.handle,
        math_ops.cast(self._learning_rate_tensor, grad.dtype),
        math_ops.cast(self._decay_tensor, grad.dtype),
        math_ops.cast(self._momentum_tensor, grad.dtype),
        math_ops.cast(self._epsilon_tensor, grad.dtype),
        grad,
        indices,
        use_locking=self._use_locking))
