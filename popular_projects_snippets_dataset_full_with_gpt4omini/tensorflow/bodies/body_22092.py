# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
update_biased = state_ops.assign_sub(biased_var,
                                     (biased_var - value) * decay)
update_local_step = local_step.assign_add(1)

# This function gets `1 - decay`, so use `1.0 - decay` in the exponent.
bias_factor = 1 - math_ops.pow(1.0 - decay, update_local_step)
exit(state_ops.assign(
    v, update_biased / bias_factor, name=ops.get_name_scope() + "/"))
