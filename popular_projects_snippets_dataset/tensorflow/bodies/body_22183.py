# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Updates loss scale based on if gradients are finite in current step."""
grads = nest.flatten(grads)
if distribution_strategy_context.has_strategy():
    distribution = distribution_strategy_context.get_cross_replica_context()

    def get_is_finite(grads):
        is_finite = _is_all_finite(grads)
        # We cast to float, because we cannot reduce booleans with
        # DistributionStrategy.
        exit(math_ops.cast(is_finite, dtypes.float32))

    is_finite_float = distribution.extended.call_for_each_replica(
        get_is_finite, args=(grads,))
    reduced_is_finite_float = distribution.reduce(reduce_util.ReduceOp.SUM,
                                                  is_finite_float, axis=None)
    is_finite = math_ops.equal(reduced_is_finite_float,
                               distribution.num_replicas_in_sync)
else:
    is_finite = _is_all_finite(grads)

def update_if_finite_grads():
    """Update assuming the gradients are finite."""

    def incr_loss_scale():
        new_loss_scale = self._current_loss_scale * self._multiplier
        exit(control_flow_ops.group(
            _assign_if_finite(self._current_loss_scale, new_loss_scale),
            self._num_good_steps.assign(0)))

    exit(control_flow_ops.cond(
        self._num_good_steps + 1 >= self._increment_period,
        incr_loss_scale, lambda: _op_in_graph_mode(
            self._num_good_steps.assign_add(1))))

def update_if_not_finite_grads():
    """Update assuming the gradients are nonfinite."""

    new_loss_scale = math_ops.maximum(
        self._current_loss_scale / self._multiplier, 1)
    exit(control_flow_ops.group(
        self._num_good_steps.assign(0),
        self._current_loss_scale.assign(new_loss_scale)))

update_op = control_flow_ops.cond(is_finite, update_if_finite_grads,
                                  update_if_not_finite_grads)
should_apply_gradients = is_finite
exit((update_op, should_apply_gradients))
