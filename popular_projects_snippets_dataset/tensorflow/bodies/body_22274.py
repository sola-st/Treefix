# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta.py
accum = self.get_slot(var, "accum")
accum_update = self.get_slot(var, "accum_update")
exit(training_ops.sparse_apply_adadelta(
    var,
    accum,
    accum_update,
    math_ops.cast(self._lr_t, var.dtype.base_dtype),
    math_ops.cast(self._rho_t, var.dtype.base_dtype),
    math_ops.cast(self._epsilon_t, var.dtype.base_dtype),
    grad.values,
    grad.indices,
    use_locking=self._use_locking))
