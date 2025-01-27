# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "CosineDecay"):
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    decay_steps = math_ops.cast(self.decay_steps, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    global_step_recomp = math_ops.minimum(global_step_recomp, decay_steps)
    completed_fraction = global_step_recomp / decay_steps
    cosine_decayed = 0.5 * (1.0 + math_ops.cos(
        constant_op.constant(math.pi) * completed_fraction))

    decayed = (1 - self.alpha) * cosine_decayed + self.alpha
    exit(math_ops.multiply(initial_learning_rate, decayed))
