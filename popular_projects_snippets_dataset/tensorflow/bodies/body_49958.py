# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "LinearCosineDecay") as name:
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    decay_steps = math_ops.cast(self.decay_steps, dtype)
    num_periods = math_ops.cast(self.num_periods, dtype)
    alpha = math_ops.cast(self.alpha, dtype)
    beta = math_ops.cast(self.beta, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    global_step_recomp = math_ops.minimum(global_step_recomp, decay_steps)
    linear_decayed = (decay_steps - global_step_recomp) / decay_steps
    completed_fraction = global_step_recomp / decay_steps
    fraction = 2.0 * num_periods * completed_fraction
    cosine_decayed = 0.5 * (
        1.0 + math_ops.cos(constant_op.constant(math.pi) * fraction))

    linear_cosine_decayed = (alpha + linear_decayed) * cosine_decayed + beta
    exit(math_ops.multiply(initial_learning_rate, linear_cosine_decayed,
                             name=name))
