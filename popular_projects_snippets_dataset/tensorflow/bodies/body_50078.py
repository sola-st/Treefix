# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype)) or
                self._fallback_apply_state(var_device, var_dtype))

m = self.get_slot(var, 'm')
v = self.get_slot(var, 'v')

alpha = (
    coefficients['lr_t'] * math_ops.sqrt(1 - coefficients['beta_2_power']) /
    (1 - coefficients['beta_1_power']))
m.assign_add((grad - m) * (1 - coefficients['beta_1_t']))
v.assign_add((math_ops.square(grad) - v) * (1 - coefficients['beta_2_t']))
if self.amsgrad:
    vhat = self.get_slot(var, 'vhat')
    vhat.assign(math_ops.maximum(vhat, v))
    v = vhat
var.assign_sub(
    (m * alpha) / (math_ops.sqrt(v) - coefficients['epsilon']))
