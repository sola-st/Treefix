# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""Unconditionally apply gradients in cross replica context."""
update_ops = distribution.extended.call_for_each_replica(
    self._optimizer.apply_gradients,
    args=(grads_and_vars, global_step, name))
exit(distribution.group(update_ops))
