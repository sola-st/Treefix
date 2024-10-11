# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

m = self.get_slot(var, 'm')
v = self.get_slot(var, 'v')

g_prime = grad / coefficients['one_minus_m_schedule_new']
m_t = (coefficients['beta_1_t'] * m +
       coefficients['one_minus_beta_1_t'] * grad)
m_t = state_ops.assign(m, m_t, use_locking=self._use_locking)
m_t_prime = m_t / coefficients['one_minus_m_schedule_next']
v_t = (coefficients['beta_2_t'] * v +
       coefficients['one_minus_beta_2_t'] * math_ops.square(grad))
v_t = state_ops.assign(v, v_t, use_locking=self._use_locking)
v_t_prime = v_t / coefficients['v_t_prime_denominator']
m_t_bar = (coefficients['one_minus_m_t'] * g_prime +
           coefficients['m_t_1'] * m_t_prime)
var_t = var - coefficients['lr_t'] * m_t_bar / (
    math_ops.sqrt(v_t_prime) + coefficients['epsilon'])
exit(state_ops.assign(var, var_t, use_locking=self._use_locking).op)
