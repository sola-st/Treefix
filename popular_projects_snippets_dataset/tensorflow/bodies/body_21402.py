# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop.py
rms = self.get_slot(var, "rms")
mom = self.get_slot(var, "momentum")
if self._centered:
    mg = self.get_slot(var, "mg")
    exit(training_ops.sparse_apply_centered_rms_prop(
        var,
        mg,
        rms,
        mom,
        math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
        math_ops.cast(self._decay_tensor, var.dtype.base_dtype),
        math_ops.cast(self._momentum_tensor, var.dtype.base_dtype),
        math_ops.cast(self._epsilon_tensor, var.dtype.base_dtype),
        grad.values,
        grad.indices,
        use_locking=self._use_locking))
else:
    exit(training_ops.sparse_apply_rms_prop(
        var,
        rms,
        mom,
        math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
        math_ops.cast(self._decay_tensor, var.dtype.base_dtype),
        math_ops.cast(self._momentum_tensor, var.dtype.base_dtype),
        math_ops.cast(self._epsilon_tensor, var.dtype.base_dtype),
        grad.values,
        grad.indices,
        use_locking=self._use_locking))
