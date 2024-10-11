# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
"""Mimics the `OptimizerV2.minimize` API."""
if not callable(loss) and tape is None:
    raise ValueError('`tape` is required when a `Tensor` loss is passed.')
tape = tape if tape is not None else backprop.GradientTape()

if callable(loss):
    with tape:
        if not callable(var_list):
            tape.watch(var_list)
        loss = loss()
        if callable(var_list):
            var_list = var_list()

var_list = nest.flatten(var_list)
if var_list:
    grads = tape.gradient(loss, var_list, grad_loss)
    grads_and_vars = list(zip(grads, var_list))
    self.apply_gradients(grads_and_vars)
