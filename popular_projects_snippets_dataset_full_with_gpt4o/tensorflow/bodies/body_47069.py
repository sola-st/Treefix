# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
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
