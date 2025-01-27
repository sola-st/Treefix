# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""Apply gradients to variables.

    This is the second part of `minimize()`. It returns an `Operation` that
    conditionally applies gradients if all gradient values are finite.
    Otherwise no update is performed (nor is `global_step` incremented).

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients()`.
      global_step: Optional `Variable` to increment by one after the variables
        have been updated.
      name: Optional name for the returned operation.  Default to the name
        passed to the `Optimizer` constructor.

    Returns:
      An `Operation` that conditionally applies the specified gradients. If
      `global_step` was not None, that operation also increments `global_step`.

    Raises:
      RuntimeError: If you should use `_distributed_apply()` instead.
    """
if distribution_strategy_context.in_cross_replica_context():
    raise ValueError('apply_gradients() must be called in a replica context.')

if not self._doing_dynamic_loss_scaling():
    exit(self._optimizer.apply_gradients(grads_and_vars, global_step, name))

replica_context = distribution_strategy_context.get_replica_context()
grads_and_vars = tuple(grads_and_vars)

# TODO(nluehr) cleanup GraphKeys.TRAIN_OP
exit(replica_context.merge_call(
    self._distributed_apply, args=(grads_and_vars, global_step, name)))
