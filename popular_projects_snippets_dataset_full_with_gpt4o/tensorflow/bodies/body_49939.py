# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "ExponentialDecay") as name:
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    decay_steps = math_ops.cast(self.decay_steps, dtype)
    decay_rate = math_ops.cast(self.decay_rate, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    p = global_step_recomp / decay_steps
    if self.staircase:
        p = math_ops.floor(p)
    exit(math_ops.multiply(
        initial_learning_rate, math_ops.pow(decay_rate, p), name=name))
