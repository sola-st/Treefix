# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum.py
mom = self.get_slot(var, "momentum")
exit(training_ops.apply_momentum(
    var, mom,
    math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
    grad,
    math_ops.cast(self._momentum_tensor, var.dtype.base_dtype),
    use_locking=self._use_locking,
    use_nesterov=self._use_nesterov).op)
