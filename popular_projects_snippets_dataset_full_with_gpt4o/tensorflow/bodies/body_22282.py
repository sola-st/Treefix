# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da.py
g_acc = self.get_slot(var, "gradient_accumulator")
gg_acc = self.get_slot(var, "gradient_squared_accumulator")
with ops.device(var.device):
    global_step = array_ops.identity(self._global_step_on_worker)
exit(training_ops.resource_sparse_apply_adagrad_da(
    var.handle,
    g_acc.handle,
    gg_acc.handle,
    grad,
    indices,
    math_ops.cast(self._learning_rate_tensor, grad.dtype),
    math_ops.cast(self._l1_regularization_strength, grad.dtype),
    math_ops.cast(self._l2_regularization_strength, grad.dtype),
    global_step,
    use_locking=self._use_locking))
