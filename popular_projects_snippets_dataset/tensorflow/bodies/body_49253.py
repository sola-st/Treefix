# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
grads = self.get_gradients(loss, params)
self.updates = [state_ops.assign_add(self.iterations, 1)]

lr = self.lr
if self.initial_decay > 0:
    lr = lr * (
        1. /
        (1. +
         self.decay * math_ops.cast(self.iterations,
                                    backend.dtype(self.decay))))
# momentum
moments = self._create_all_weights(params)
for p, g, m in zip(params, grads, moments):
    v = self.momentum * m - lr * g  # velocity
    self.updates.append(state_ops.assign(m, v))

    if self.nesterov:
        new_p = p + self.momentum * v - lr * g
    else:
        new_p = p + v

    # Apply constraints.
    if getattr(p, 'constraint', None) is not None:
        new_p = p.constraint(new_p)

    self.updates.append(state_ops.assign(p, new_p))
exit(self.updates)
