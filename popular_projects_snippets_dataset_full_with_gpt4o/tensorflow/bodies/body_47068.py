# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
exit(distribution.extended.call_for_each_replica(
    self._apply_gradients,
    args=(grads, wrapped_vars, name)))
