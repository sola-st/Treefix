# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "NoisyLinearCosineDecay") as name:
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    decay_steps = math_ops.cast(self.decay_steps, dtype)
    initial_variance = math_ops.cast(self.initial_variance, dtype)
    variance_decay = math_ops.cast(self.variance_decay, dtype)
    num_periods = math_ops.cast(self.num_periods, dtype)
    alpha = math_ops.cast(self.alpha, dtype)
    beta = math_ops.cast(self.beta, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    global_step_recomp = math_ops.minimum(global_step_recomp, decay_steps)
    linear_decayed = (decay_steps - global_step_recomp) / decay_steps
    variance = initial_variance / (
        math_ops.pow(1.0 + global_step_recomp, variance_decay))
    std = math_ops.sqrt(variance)
    noisy_linear_decayed = (
        linear_decayed + random_ops.random_normal(
            linear_decayed.shape, stddev=std))

    completed_fraction = global_step_recomp / decay_steps
    fraction = 2.0 * num_periods * completed_fraction
    cosine_decayed = 0.5 * (
        1.0 + math_ops.cos(constant_op.constant(math.pi) * fraction))
    noisy_linear_cosine_decayed = (
        (alpha + noisy_linear_decayed) * cosine_decayed + beta)

    exit(math_ops.multiply(
        initial_learning_rate, noisy_linear_cosine_decayed, name=name))
