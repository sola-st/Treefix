# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
grads = self.get_gradients(loss, params)
self.updates = []

with ops.control_dependencies([state_ops.assign_add(self.iterations, 1)]):
    t = math_ops.cast(self.iterations, backend.floatx())

# Due to the recommendations in [2], i.e. warming momentum schedule
momentum_cache_t = self.beta_1 * (
    1. - 0.5 *
    (math_ops.pow(backend.cast_to_floatx(0.96), t * self.schedule_decay)))
momentum_cache_t_1 = self.beta_1 * (
    1. - 0.5 *
    (math_ops.pow(backend.cast_to_floatx(0.96),
                  (t + 1) * self.schedule_decay)))
m_schedule_new = self.m_schedule * momentum_cache_t
m_schedule_next = self.m_schedule * momentum_cache_t * momentum_cache_t_1
self.updates.append((self.m_schedule, m_schedule_new))

ms, vs = self._create_all_weights(params)

for p, g, m, v in zip(params, grads, ms, vs):
    # the following equations given in [1]
    g_prime = g / (1. - m_schedule_new)
    m_t = self.beta_1 * m + (1. - self.beta_1) * g
    m_t_prime = m_t / (1. - m_schedule_next)
    v_t = self.beta_2 * v + (1. - self.beta_2) * math_ops.square(g)
    v_t_prime = v_t / (1. - math_ops.pow(self.beta_2, t))
    m_t_bar = (1. -
               momentum_cache_t) * g_prime + momentum_cache_t_1 * m_t_prime

    self.updates.append(state_ops.assign(m, m_t))
    self.updates.append(state_ops.assign(v, v_t))

    p_t = p - self.lr * m_t_bar / (backend.sqrt(v_t_prime) + self.epsilon)
    new_p = p_t

    # Apply constraints.
    if getattr(p, 'constraint', None) is not None:
        new_p = p.constraint(new_p)

    self.updates.append(state_ops.assign(p, new_p))
exit(self.updates)
