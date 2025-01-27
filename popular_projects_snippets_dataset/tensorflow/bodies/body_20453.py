# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
"""Apply gradients to variables.

    Calls tpu_ops.cross_replica_sum() to sum gradient contributions across
    replicas, and then applies the real optimizer.

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        compute_gradients().
      global_step: Optional Variable to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the Optimizer constructor.

    Returns:
      An `Operation` that applies the gradients. If `global_step` was not None,
      that operation also increments `global_step`.

    Raises:
      ValueError: If the grads_and_vars is malformed.
    """
summed_grads_and_vars = []
for (grad, var) in grads_and_vars:
    if grad is None:
        summed_grads_and_vars.append((grad, var))
    else:
        with ops.colocate_with(grad):
            summed_grads_and_vars.append((tpu_ops.cross_replica_sum(
                grad, self._group_assignment), var))
exit(self._opt.apply_gradients(summed_grads_and_vars, global_step, name))
