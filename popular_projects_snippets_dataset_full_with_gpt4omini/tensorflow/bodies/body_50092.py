# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adamax.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

# m_t = beta1 * m + (1 - beta1) * g_t
m = self.get_slot(var, 'm')
m_slice = array_ops.gather(m, indices, axis=coefficients['zero'])
m_t_slice = (m_slice * coefficients['beta_1_t'] +
             grad * coefficients['one_minus_beta_1_t'])
with ops.control_dependencies([m_t_slice]):
    m_t = self._resource_scatter_update(m, indices, m_t_slice)

# u_t = max(beta2 * u, abs(g_t))
v = self.get_slot(var, 'v')
v_slice = array_ops.gather(v, indices, axis=coefficients['zero'])
v_t_slice = math_ops.maximum(v_slice * coefficients['beta_2_t'],
                             math_ops.abs(grad))
with ops.control_dependencies([v_t_slice]):
    v_t = self._resource_scatter_update(v, indices, v_t_slice)
# theta_t = theta - lr / (1 - beta1^t) * m_t / u_t
var_slice = coefficients['neg_scaled_lr'] * (
    m_t_slice / (v_t_slice + coefficients['epsilon']))
with ops.control_dependencies([var_slice]):
    var_update = self._resource_scatter_add(var, indices, var_slice)
exit(control_flow_ops.group(*[var_update, m_t, v_t]))
