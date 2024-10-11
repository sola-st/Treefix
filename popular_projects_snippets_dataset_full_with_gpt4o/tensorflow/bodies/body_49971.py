# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

acc = self.get_slot(var, 'accumulator')
exit(gen_training_ops.ResourceSparseApplyAdagradV2(
    var=var.handle,
    accum=acc.handle,
    lr=coefficients['lr_t'],
    epsilon=coefficients['epsilon'],
    grad=grad,
    indices=indices,
    use_locking=self._use_locking))
