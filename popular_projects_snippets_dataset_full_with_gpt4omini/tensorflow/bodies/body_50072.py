# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

# m_t = beta1 * m + (1 - beta1) * g_t
m = self.get_slot(var, 'm')
m_scaled_g_values = grad * coefficients['one_minus_beta_1_t']
m_t = state_ops.assign(m, m * coefficients['beta_1_t'],
                       use_locking=self._use_locking)
with ops.control_dependencies([m_t]):
    m_t = self._resource_scatter_add(m, indices, m_scaled_g_values)

# v_t = beta2 * v + (1 - beta2) * (g_t * g_t)
v = self.get_slot(var, 'v')
v_scaled_g_values = (grad * grad) * coefficients['one_minus_beta_2_t']
v_t = state_ops.assign(v, v * coefficients['beta_2_t'],
                       use_locking=self._use_locking)
with ops.control_dependencies([v_t]):
    v_t = self._resource_scatter_add(v, indices, v_scaled_g_values)

if not self.amsgrad:
    v_sqrt = math_ops.sqrt(v_t)
    var_update = state_ops.assign_sub(
        var, coefficients['lr'] * m_t / (v_sqrt + coefficients['epsilon']),
        use_locking=self._use_locking)
    exit(control_flow_ops.group(*[var_update, m_t, v_t]))
else:
    v_hat = self.get_slot(var, 'vhat')
    v_hat_t = math_ops.maximum(v_hat, v_t)
    with ops.control_dependencies([v_hat_t]):
        v_hat_t = state_ops.assign(
            v_hat, v_hat_t, use_locking=self._use_locking)
    v_hat_sqrt = math_ops.sqrt(v_hat_t)
    var_update = state_ops.assign_sub(
        var,
        coefficients['lr'] * m_t / (v_hat_sqrt + coefficients['epsilon']),
        use_locking=self._use_locking)
    exit(control_flow_ops.group(*[var_update, m_t, v_t, v_hat_t]))
