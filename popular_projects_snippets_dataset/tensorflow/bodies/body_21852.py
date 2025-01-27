# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl.py
accum = self.get_slot(var, "accum")
linear = self.get_slot(var, "linear")
if self._l2_shrinkage_regularization_strength <= 0.0:
    exit(training_ops.resource_sparse_apply_ftrl(
        var.handle,
        accum.handle,
        linear.handle,
        grad,
        indices,
        math_ops.cast(self._learning_rate_tensor, grad.dtype),
        math_ops.cast(self._l1_regularization_strength_tensor, grad.dtype),
        math_ops.cast(self._adjusted_l2_regularization_strength_tensor,
                      grad.dtype),
        math_ops.cast(self._learning_rate_power_tensor, grad.dtype),
        use_locking=self._use_locking))
else:
    exit(training_ops.resource_sparse_apply_ftrl_v2(
        var.handle,
        accum.handle,
        linear.handle,
        grad,
        indices,
        math_ops.cast(self._learning_rate_tensor, grad.dtype),
        math_ops.cast(self._l1_regularization_strength_tensor, grad.dtype),
        math_ops.cast(self._adjusted_l2_regularization_strength_tensor,
                      grad.dtype),
        math_ops.cast(self._l2_shrinkage_regularization_strength_tensor,
                      grad.dtype),
        math_ops.cast(self._learning_rate_power_tensor, grad.dtype),
        use_locking=self._use_locking))
