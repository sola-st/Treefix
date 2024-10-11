# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
grads = self.get_gradients(loss, params)
self.updates = [state_ops.assign_add(self.iterations, 1)]
accumulators, delta_accumulators = self._create_all_weights(params)

lr = self.lr
if self.initial_decay > 0:
    lr = lr * (
        1. /
        (1. +
         self.decay * math_ops.cast(self.iterations,
                                    backend.dtype(self.decay))))

for p, g, a, d_a in zip(params, grads, accumulators, delta_accumulators):
    # update accumulator
    new_a = self.rho * a + (1. - self.rho) * math_ops.square(g)
    self.updates.append(state_ops.assign(a, new_a))

    # use the new accumulator and the *old* delta_accumulator
    update = g * backend.sqrt(d_a + self.epsilon) / backend.sqrt(
        new_a + self.epsilon)
    new_p = p - lr * update

    # Apply constraints.
    if getattr(p, 'constraint', None) is not None:
        new_p = p.constraint(new_p)

    self.updates.append(state_ops.assign(p, new_p))

    # update delta_accumulator
    new_d_a = self.rho * d_a + (1 - self.rho) * math_ops.square(update)
    self.updates.append(state_ops.assign(d_a, new_d_a))
exit(self.updates)
