# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adamax.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

m = self.get_slot(var, 'm')
v = self.get_slot(var, 'v')
exit(gen_training_ops.ResourceApplyAdaMax(
    var=var.handle,
    m=m.handle,
    v=v.handle,
    beta1_power=coefficients['beta_1_power'],
    lr=coefficients['lr_t'],
    beta1=coefficients['beta_1_t'],
    beta2=coefficients['beta_2_t'],
    epsilon=coefficients['epsilon'],
    grad=grad,
    use_locking=self._use_locking))
