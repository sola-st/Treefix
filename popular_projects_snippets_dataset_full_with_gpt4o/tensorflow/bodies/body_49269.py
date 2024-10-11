# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
grads = self.get_gradients(loss, params)
self.updates = []

lr = self.lr
if self.initial_decay > 0:
    lr = lr * (
        1. /
        (1. +
         self.decay * math_ops.cast(self.iterations,
                                    backend.dtype(self.decay))))

with ops.control_dependencies([state_ops.assign_add(self.iterations, 1)]):
    t = math_ops.cast(self.iterations, backend.floatx())
lr_t = lr * (
    backend.sqrt(1. - math_ops.pow(self.beta_2, t)) /
    (1. - math_ops.pow(self.beta_1, t)))

ms, vs, vhats = self._create_all_weights(params)
for p, g, m, v, vhat in zip(params, grads, ms, vs, vhats):
    m_t = (self.beta_1 * m) + (1. - self.beta_1) * g
    v_t = (self.beta_2 * v) + (1. - self.beta_2) * math_ops.square(g)
    if self.amsgrad:
        vhat_t = math_ops.maximum(vhat, v_t)
        p_t = p - lr_t * m_t / (backend.sqrt(vhat_t) + self.epsilon)
        self.updates.append(state_ops.assign(vhat, vhat_t))
    else:
        p_t = p - lr_t * m_t / (backend.sqrt(v_t) + self.epsilon)

    self.updates.append(state_ops.assign(m, m_t))
    self.updates.append(state_ops.assign(v, v_t))
    new_p = p_t

    # Apply constraints.
    if getattr(p, 'constraint', None) is not None:
        new_p = p.constraint(new_p)

    self.updates.append(state_ops.assign(p, new_p))
exit(self.updates)
