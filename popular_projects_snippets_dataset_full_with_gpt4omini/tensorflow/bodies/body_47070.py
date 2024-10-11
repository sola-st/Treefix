# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
if distribution_strategy_context.in_cross_replica_context():
    raise ValueError('apply_gradients() must be called in a replica context.')
# We check for the strategy here despite already checking in the constructor
# as frequently the optimizer is created outside the strategy's scope.
self._raise_if_strategy_unsupported()

grads_and_vars = optimizer_utils.filter_empty_gradients(grads_and_vars)
if experimental_aggregate_gradients:
    # We must aggregate the gradients here instead of in
    # self.optimizer.apply_gradients, so that any NaN or Inf gradients are
    # propogated to each replica. If any replica has a NaN or Inf gradient,
    # they must all have a NaN or Inf gradient so that they all skip the step.
    # pylint: disable=protected-access
    grads_and_vars = self._optimizer._transform_unaggregated_gradients(
        grads_and_vars)
    grads_and_vars = self._optimizer._aggregate_gradients(grads_and_vars)
    # pylint: enable=protected-access

grads_and_vars = tuple(grads_and_vars)
grads = [g for g, _ in grads_and_vars]
# We do not want DistributionStrategy to unwrap any MirroredVariables in
# grads_and_vars, because even in a replica context, the wrapped
# optimizer expects mirrored variables. So we wrap the variables with an
# _UnwrapPreventer, preventing DistributionStrategy from unwrapping the
# MirroredVariables.
wrapped_vars = _UnwrapPreventer([v for _, v in grads_and_vars])

def do_not_apply_fn():
    # Normally self._optimizer.iterations is incremented in
    # self._optimizer.apply_gradients(). Since that is not called in this
    # branch, we increment it here instead.
    exit(self._optimizer.iterations.assign_add(1, read_value=False))

def _if_should_apply_grads(grads):
    if isinstance(self._loss_scale, _DynamicLossScaleState):
        exit(self._loss_scale.update(grads))
    else:
        exit((control_flow_ops.no_op(), True))

if optimizer_utils.strategy_supports_no_merge_call():
    loss_scale_update_op, should_apply_grads = _if_should_apply_grads(grads)
    def apply_fn():
        exit(self._apply_gradients(grads, wrapped_vars, name))

    maybe_apply_op = smart_cond.smart_cond(should_apply_grads, apply_fn,
                                           do_not_apply_fn)
    exit(control_flow_ops.group(maybe_apply_op, loss_scale_update_op))

else:

    def _apply_gradients_cross_replica(distribution, grads, wrapped_vars,
                                       name):
        loss_scale_update_op, should_apply_grads = _if_should_apply_grads(grads)

        def apply_fn():
            exit(distribution.extended.call_for_each_replica(
                self._apply_gradients,
                args=(grads, wrapped_vars, name)))

        # Note: We must call this cond() in a cross-replica context.
        # DistributionStrategy does not support having a cond in a replica
        # context with a branch that calls `merge_call`, and
        # self._optimizer.apply_gradients calls `merge_call`.
        maybe_apply_op = smart_cond.smart_cond(should_apply_grads, apply_fn,
                                               do_not_apply_fn)
        exit(control_flow_ops.group(maybe_apply_op, loss_scale_update_op))
    exit(distribution_strategy_context.get_replica_context().merge_call(
        _apply_gradients_cross_replica,
        args=(grads, wrapped_vars, name)))
