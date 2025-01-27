# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta.py
accum = self.get_slot(var, "accum")
accum_update = self.get_slot(var, "accum_update")
exit(training_ops.resource_sparse_apply_adadelta(
    var.handle,
    accum.handle,
    accum_update.handle,
    math_ops.cast(self._lr_t, grad.dtype),
    math_ops.cast(self._rho_t, grad.dtype),
    math_ops.cast(self._epsilon_t, grad.dtype),
    grad,
    indices,
    use_locking=self._use_locking))
