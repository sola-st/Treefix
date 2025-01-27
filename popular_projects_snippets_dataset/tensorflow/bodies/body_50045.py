# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
# This method is only needed for momentum optimization.
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

momentum_var = self.get_slot(var, "momentum")
exit(gen_training_ops.ResourceSparseApplyKerasMomentum(
    var=var.handle,
    accum=momentum_var.handle,
    lr=coefficients["lr_t"],
    grad=grad,
    indices=indices,
    momentum=coefficients["momentum"],
    use_locking=self._use_locking,
    use_nesterov=self.nesterov))
