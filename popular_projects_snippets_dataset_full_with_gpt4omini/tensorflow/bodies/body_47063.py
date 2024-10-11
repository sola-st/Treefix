# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
loss = self.get_scaled_loss(loss)
grads = self._optimizer.get_gradients(loss, params)
exit(self.get_unscaled_gradients(grads))
