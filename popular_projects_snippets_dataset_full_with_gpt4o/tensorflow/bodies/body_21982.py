# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
# Update the power accumulators.
with ops.control_dependencies(update_ops):
    beta1_power, beta2_power = self._get_beta_accumulators()
    with ops.colocate_with(beta1_power):
        update_beta1 = beta1_power.assign(
            beta1_power * self._beta1_t, use_locking=self._use_locking)
        update_beta2 = beta2_power.assign(
            beta2_power * self._beta2_t, use_locking=self._use_locking)
exit(control_flow_ops.group(
    *update_ops + [update_beta1, update_beta2], name=name_scope))
