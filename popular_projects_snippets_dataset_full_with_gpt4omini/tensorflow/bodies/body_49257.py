# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
grads = self.get_gradients(loss, params)
accumulators = self._create_all_weights(params)
self.updates = [state_ops.assign_add(self.iterations, 1)]

lr = self.lr
if self.initial_decay > 0:
    lr = lr * (
        1. /
        (1. +
         self.decay * math_ops.cast(self.iterations,
                                    backend.dtype(self.decay))))

for p, g, a in zip(params, grads, accumulators):
    # update accumulator
    new_a = self.rho * a + (1. - self.rho) * math_ops.square(g)
    self.updates.append(state_ops.assign(a, new_a))
    new_p = p - lr * g / (backend.sqrt(new_a) + self.epsilon)

    # Apply constraints.
    if getattr(p, 'constraint', None) is not None:
        new_p = p.constraint(new_p)

    self.updates.append(state_ops.assign(p, new_p))
exit(self.updates)
