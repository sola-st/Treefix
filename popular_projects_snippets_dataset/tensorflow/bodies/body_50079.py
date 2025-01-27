# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype)) or
                self._fallback_apply_state(var_device, var_dtype))

# m_t = beta1 * m + (1 - beta1) * g_t
m = self.get_slot(var, 'm')
m_scaled_g_values = grad * coefficients['one_minus_beta_1_t']
m.assign(m * coefficients['beta_1_t'])
m.scatter_add(indexed_slices.IndexedSlices(m_scaled_g_values, indices))

# v_t = beta2 * v + (1 - beta2) * (g_t * g_t)
v = self.get_slot(var, 'v')
v_scaled_g_values = (grad * grad) * coefficients['one_minus_beta_2_t']
v.assign(v * coefficients['beta_2_t'])
v.scatter_add(indexed_slices.IndexedSlices(v_scaled_g_values, indices))

if not self.amsgrad:
    var.assign_sub(coefficients['lr'] * m /
                   (math_ops.sqrt(v) + coefficients['epsilon']))
else:
    v_hat = self.get_slot(var, 'vhat')
    v_hat.assign(math_ops.maximum(v_hat, v))
    var.assign_sub(coefficients['lr'] * m /
                   (math_ops.sqrt(v_hat) + coefficients['epsilon']))
