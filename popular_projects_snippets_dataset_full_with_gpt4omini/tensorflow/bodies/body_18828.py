# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Sums the weights of cases where the given values are True.

  If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

  Args:
    values: A `bool` `Tensor` of arbitrary size.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `values`, and must be broadcastable to `values` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `values` dimension).
    metrics_collections: An optional list of collections that the metric
      value variable should be added to.
    updates_collections: An optional list of collections that the metric update
      ops should be added to.

  Returns:
    value_tensor: A `Tensor` representing the current value of the metric.
    update_op: An operation that accumulates the error from a batch of data.

  Raises:
    ValueError: If `weights` is not `None` and its shape doesn't match `values`,
      or if either `metrics_collections` or `updates_collections` are not a list
      or tuple.
  """
check_ops.assert_type(values, dtypes.bool)
count = metric_variable([], dtypes.float32, name='count')

values = math_ops.cast(values, dtypes.float32)
if weights is not None:
    with ops.control_dependencies((check_ops.assert_rank_in(
        weights, (0, array_ops.rank(values))),)):
        weights = math_ops.cast(weights, dtypes.float32)
        values = math_ops.multiply(values, weights)

value_tensor = _aggregate_variable(count, metrics_collections)

update_op = state_ops.assign_add(count, math_ops.reduce_sum(values))
if updates_collections:
    ops.add_to_collections(updates_collections, update_op)

exit((value_tensor, update_op))
