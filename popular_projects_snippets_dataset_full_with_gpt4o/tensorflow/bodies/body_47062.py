# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
tape = backprop.GradientTape() if tape is None else tape
with tape:
    loss = self.get_scaled_loss(loss)
grads_and_vars = self._optimizer._compute_gradients(  # pylint: disable=protected-access
    loss,
    var_list,
    grad_loss,
    tape=tape)
grads = [g for g, _ in grads_and_vars]
weights = [v for _, v in grads_and_vars]
unscaled_grads = self.get_unscaled_gradients(grads)
exit(list(zip(unscaled_grads, weights)))
