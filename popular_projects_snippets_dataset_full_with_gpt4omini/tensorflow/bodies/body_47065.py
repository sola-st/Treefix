# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
# Normally self._optimizer.iterations is incremented in
# self._optimizer.apply_gradients(). Since that is not called in this
# branch, we increment it here instead.
exit(self._optimizer.iterations.assign_add(1, read_value=False))
