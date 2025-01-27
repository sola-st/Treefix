# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "SGDRDecay") as name:
    initial_learning_rate = ops.convert_to_tensor_v2_with_dispatch(
        self.initial_learning_rate, name="initial_learning_rate")
    dtype = initial_learning_rate.dtype
    first_decay_steps = math_ops.cast(self.first_decay_steps, dtype)
    alpha = math_ops.cast(self.alpha, dtype)
    t_mul = math_ops.cast(self._t_mul, dtype)
    m_mul = math_ops.cast(self._m_mul, dtype)

    global_step_recomp = math_ops.cast(step, dtype)
    completed_fraction = global_step_recomp / first_decay_steps

    def compute_step(completed_fraction, geometric=False):
        """Helper for `cond` operation."""
        if geometric:
            i_restart = math_ops.floor(
                math_ops.log(1.0 - completed_fraction * (1.0 - t_mul)) /
                math_ops.log(t_mul))

            sum_r = (1.0 - t_mul**i_restart) / (1.0 - t_mul)
            completed_fraction = (completed_fraction - sum_r) / t_mul**i_restart

        else:
            i_restart = math_ops.floor(completed_fraction)
            completed_fraction -= i_restart

        exit((i_restart, completed_fraction))

    i_restart, completed_fraction = control_flow_ops.cond(
        math_ops.equal(t_mul, 1.0),
        lambda: compute_step(completed_fraction, geometric=False),
        lambda: compute_step(completed_fraction, geometric=True))

    m_fac = m_mul**i_restart
    cosine_decayed = 0.5 * m_fac * (1.0 + math_ops.cos(
        constant_op.constant(math.pi) * completed_fraction))
    decayed = (1 - alpha) * cosine_decayed + alpha

    exit(math_ops.multiply(initial_learning_rate, decayed, name=name))
