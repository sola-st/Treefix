# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Apply gradients to variables.

    This is the second part of `minimize()`. It returns an `Operation` that
    applies gradients.

    The method sums gradients from all replicas in the presence of
    `tf.distribute.Strategy` by default. You can aggregate gradients yourself by
    passing `experimental_aggregate_gradients=False`.

    Example:

    ```python
    grads = tape.gradient(loss, vars)
    grads = tf.distribute.get_replica_context().all_reduce('sum', grads)
    # Processing aggregated gradients.
    optimizer.apply_gradients(zip(grads, vars),
        experimental_aggregate_gradients=False)

    ```

    Args:
      grads_and_vars: List of (gradient, variable) pairs.
      name: Optional name for the returned operation. Default to the name passed
        to the `Optimizer` constructor.
      experimental_aggregate_gradients: Whether to sum gradients from different
        replicas in the presense of `tf.distribute.Strategy`. If False, it's
        user responsibility to aggregate the gradients. Default to True.

    Returns:
      An `Operation` that applies the specified gradients. The `iterations`
      will be automatically increased by 1.

    Raises:
      TypeError: If `grads_and_vars` is malformed.
      ValueError: If none of the variables have gradients.
      RuntimeError: If called in a cross-replica context.
    """
grads_and_vars = optimizer_utils.filter_empty_gradients(grads_and_vars)
var_list = [v for (_, v) in grads_and_vars]

with ops.name_scope_v2(self._name):
    # Create iteration if necessary.
    with ops.init_scope():
        self._create_all_weights(var_list)

    if not grads_and_vars:
        # Distribution strategy does not support reducing an empty list of
        # gradients
        exit(control_flow_ops.no_op())

    if distribute_ctx.in_cross_replica_context():
        raise RuntimeError(
            "`apply_gradients() cannot be called in cross-replica context. "
            "Use `tf.distribute.Strategy.run` to enter replica "
            "context.")

    strategy = distribute_ctx.get_strategy()
    if (not experimental_aggregate_gradients and strategy and
        isinstance(strategy,
                   (parameter_server_strategy.ParameterServerStrategyV1,
                    parameter_server_strategy_v2.ParameterServerStrategyV2,
                    central_storage_strategy.CentralStorageStrategy,
                    central_storage_strategy.CentralStorageStrategyV1))):
        raise NotImplementedError(
            "`experimental_aggregate_gradients=False is not supported for "
            "ParameterServerStrategy and CentralStorageStrategy")

    apply_state = self._prepare(var_list)
    if experimental_aggregate_gradients:
        grads_and_vars = self._transform_unaggregated_gradients(grads_and_vars)
        grads_and_vars = self._aggregate_gradients(grads_and_vars)
    grads_and_vars = self._transform_gradients(grads_and_vars)

    if optimizer_utils.strategy_supports_no_merge_call():
        exit(self._distributed_apply(strategy, grads_and_vars, name,
                                       apply_state))
    else:
        exit(distribute_ctx.get_replica_context().merge_call(
            functools.partial(self._distributed_apply, apply_state=apply_state),
            args=(grads_and_vars,),
            kwargs={
                "name": name,
            }))
