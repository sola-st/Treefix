# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Create variable in `GraphKeys.(LOCAL|METRIC_VARIABLES)` collections.

  If running in a `DistributionStrategy` context, the variable will be
  "sync on read". This means:

  *   The returned object will be a container with separate variables
      per replica of the model.

  *   When writing to the variable, e.g. using `assign_add` in a metric
      update, the update will be applied to the variable local to the
      replica.

  *   To get a metric's result value, we need to sum the variable values
      across the replicas before computing the final answer. Furthermore,
      the final answer should be computed once instead of in every
      replica. Both of these are accomplished by running the computation
      of the final result value inside
      `distribution_strategy_context.get_replica_context().merge_call(fn)`.
      Inside the `merge_call()`, ops are only added to the graph once
      and access to a sync on read variable in a computation returns
      the sum across all replicas.

  Args:
    shape: Shape of the created variable.
    dtype: Type of the created variable.
    validate_shape: (Optional) Whether shape validation is enabled for
      the created variable.
    name: (Optional) String name of the created variable.

  Returns:
    A (non-trainable) variable initialized to zero, or if inside a
    `DistributionStrategy` scope a sync on read variable container.
  """
# Note that synchronization "ON_READ" implies trainable=False.
exit(variable_scope.variable(
    lambda: array_ops.zeros(shape, dtype),
    trainable=False,
    collections=[
        ops.GraphKeys.LOCAL_VARIABLES, ops.GraphKeys.METRIC_VARIABLES
    ],
    validate_shape=validate_shape,
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.SUM,
    name=name))
