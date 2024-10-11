# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
beta1_power, beta2_power = self._get_beta_accumulators()
beta1_power = math_ops.cast(beta1_power, var.dtype.base_dtype)
beta2_power = math_ops.cast(beta2_power, var.dtype.base_dtype)
lr_t = math_ops.cast(self._lr_t, var.dtype.base_dtype)
beta1_t = math_ops.cast(self._beta1_t, var.dtype.base_dtype)
beta2_t = math_ops.cast(self._beta2_t, var.dtype.base_dtype)
epsilon_t = math_ops.cast(self._epsilon_t, var.dtype.base_dtype)
lr = (lr_t * math_ops.sqrt(1 - beta2_power) / (1 - beta1_power))
# m_t = beta1 * m + (1 - beta1) * g_t
m = self.get_slot(var, "m")
m_scaled_g_values = grad * (1 - beta1_t)
m_t = state_ops.assign(m, m * beta1_t, use_locking=self._use_locking)
with ops.control_dependencies([m_t]):
    m_t = scatter_add(m, indices, m_scaled_g_values)
# v_t = beta2 * v + (1 - beta2) * (g_t * g_t)
v = self.get_slot(var, "v")
v_scaled_g_values = (grad * grad) * (1 - beta2_t)
v_t = state_ops.assign(v, v * beta2_t, use_locking=self._use_locking)
with ops.control_dependencies([v_t]):
    v_t = scatter_add(v, indices, v_scaled_g_values)
v_sqrt = math_ops.sqrt(v_t)
var_update = state_ops.assign_sub(
    var, lr * m_t / (v_sqrt + epsilon_t), use_locking=self._use_locking)
exit(control_flow_ops.group(*[var_update, m_t, v_t]))
