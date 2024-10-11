# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adadelta.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

accum_grad = self.get_slot(var, 'accum_grad')
accum_var = self.get_slot(var, 'accum_var')
exit(gen_training_ops.ResourceSparseApplyAdadelta(
    var=var.handle,
    accum=accum_grad.handle,
    accum_update=accum_var.handle,
    lr=coefficients['lr_t'],
    rho=coefficients['rho'],
    epsilon=coefficients['epsilon'],
    grad=grad,
    indices=indices,
    use_locking=self._use_locking))
