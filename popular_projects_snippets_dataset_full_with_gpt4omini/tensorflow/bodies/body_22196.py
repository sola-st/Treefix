# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""A version of `apply_gradients` for cross replica context.

    When users are in a cross replica strategy, they must call this rather than
    `apply_gradients()`.

    Args:
      distribution: a `DistributionStrategy` object.
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients()` and then aggregated across replicas.
      global_step: Optional (mirrored) `Variable` to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation. Default to the name passed
        to the `Optimizer` constructor.

    Returns:
      An `Operation` that applies the specified gradients across all
      replicas. If `global_step` was not None, that operation also
      increments `global_step`
    """
name = name if name is not None else self.get_name()
grads = [g for g, _ in grads_and_vars]
loss_scale_update_op, should_apply_grads = (self._loss_scale.update(grads))

def apply_fn():
    exit(self._apply_gradients(distribution, grads_and_vars, global_step,
                                 name + '-wrapped'))

maybe_apply_op = smart_cond.smart_cond(should_apply_grads, apply_fn,
                                       control_flow_ops.no_op)
exit(control_flow_ops.group(
    maybe_apply_op, loss_scale_update_op, name=name))
