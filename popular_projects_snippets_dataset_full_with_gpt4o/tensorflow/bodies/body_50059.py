# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

m = self.get_slot(var, 'm')
v = self.get_slot(var, 'v')

g_prime = grad / coefficients['one_minus_m_schedule_new']

# m_t = beta1 * m + (1 - beta1) * g_t
m_scaled_g_values = grad * coefficients['one_minus_beta_1_t']
m_t = state_ops.assign(m, m * coefficients['beta_1_t'],
                       use_locking=self._use_locking)

with ops.control_dependencies([m_t]):
    m_t = self._resource_scatter_add(m, indices, m_scaled_g_values)
    m_t_slice = array_ops.gather(m_t, indices)

m_t_prime = m_t_slice / coefficients['one_minus_m_schedule_next']
m_t_bar = (coefficients['one_minus_m_t'] * g_prime +
           coefficients['m_t_1'] * m_t_prime)

# v_t = beta2 * v + (1 - beta2) * (g_t * g_t)
v_scaled_g_values = (grad * grad) * coefficients['one_minus_beta_2_t']
v_t = state_ops.assign(v, v * coefficients['beta_2_t'],
                       use_locking=self._use_locking)

with ops.control_dependencies([v_t]):
    v_t = self._resource_scatter_add(v, indices, v_scaled_g_values)
    v_t_slice = array_ops.gather(v_t, indices)

v_t_prime = v_t_slice / coefficients['v_t_prime_denominator']
v_prime_sqrt_plus_eps = math_ops.sqrt(v_t_prime) + coefficients['epsilon']

var_update = self._resource_scatter_add(
    var, indices,
    coefficients['neg_lr_t'] * m_t_bar / v_prime_sqrt_plus_eps)
exit(control_flow_ops.group(*[var_update, m_t_bar, v_t]))
