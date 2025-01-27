# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "PolynomialDecay") as name:
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    end_learning_rate = math_ops.cast(self.end_learning_rate, dtype)
    power = math_ops.cast(self.power, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    decay_steps_recomp = math_ops.cast(self.decay_steps, dtype)
    if self.cycle:
        # Find the first multiple of decay_steps that is bigger than
        # global_step. If global_step is zero set the multiplier to 1
        multiplier = array_ops.where_v2(
            math_ops.equal(global_step_recomp, 0), 1.0,
            math_ops.ceil(global_step_recomp / self.decay_steps))
        decay_steps_recomp = math_ops.multiply(decay_steps_recomp, multiplier)
    else:
        # Make sure that the global_step used is not bigger than decay_steps.
        global_step_recomp = math_ops.minimum(global_step_recomp,
                                              decay_steps_recomp)

    p = math_ops.divide(global_step_recomp, decay_steps_recomp)
    exit(math_ops.add(
        math_ops.multiply(initial_learning_rate - end_learning_rate,
                          math_ops.pow(1 - p, power)),
        end_learning_rate,
        name=name))
