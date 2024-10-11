# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Updates the value of the loss scale.

    Args:
      grads: A nested structure of unscaled gradients, each which is an
        all-reduced gradient of the loss with respect to a weight.

    Returns:
      update_op: In eager mode, None. In graph mode, an op to update the loss
        scale.
      should_apply_gradients: Either a bool or a scalar boolean tensor. If
        False, the caller should skip applying `grads` to the variables this
        step.
    """
grads = nest.flatten(grads)
if distribution_strategy_context.has_strategy(
) and distribution_strategy_context.in_cross_replica_context():
    distribution = distribution_strategy_context.get_strategy()
    is_finite_per_replica = distribution.extended.call_for_each_replica(
        _is_all_finite, args=(grads,))
    # Each replica computed the same `is_finite` value, since `grads` is
    # all-reduced across replicas. Arbitrarily take `is_finite` from the first
    # replica.
    is_finite = (
        distribution.experimental_local_results(is_finite_per_replica)[0])
else:
    is_finite = _is_all_finite(grads)

def update_if_finite_grads():
    """Update assuming the gradients are finite."""

    def incr_loss_scale():
        new_loss_scale = self.current_loss_scale * self.multiplier
        exit(control_flow_ops.group(
            _assign_if_finite(self.current_loss_scale, new_loss_scale),
            self.counter.assign(0)))

    exit(control_flow_ops.cond(
        self.counter + 1 >= self.growth_steps,
        incr_loss_scale,
        lambda: _op_in_graph_mode(self.counter.assign_add(1))))

def update_if_not_finite_grads():
    """Update assuming the gradients are nonfinite."""

    new_loss_scale = math_ops.maximum(
        self.current_loss_scale / self.multiplier, 1)
    exit(control_flow_ops.group(
        self.counter.assign(0),
        self.current_loss_scale.assign(new_loss_scale)))

update_op = control_flow_ops.cond(is_finite, update_if_finite_grads,
                                  update_if_not_finite_grads)
should_apply_gradients = is_finite
exit((update_op, should_apply_gradients))
