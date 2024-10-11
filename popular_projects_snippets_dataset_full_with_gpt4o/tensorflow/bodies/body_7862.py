# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""Perform a deepcopy of the `AggregatingVariable`.

    Unlike the deepcopy of a regular tf.Variable, this keeps the original
    strategy and devices of the `AggregatingVariable`.  To avoid confusion
    with the behavior of deepcopy on a regular `Variable` (which does
    copy into new devices), we only allow a deepcopy of a `AggregatingVariable`
    within its originating strategy scope.

    Args:
      memo: The memoization object for `deepcopy`.

    Returns:
      A deep copy of the current `AggregatingVariable`.

    Raises:
      RuntimeError: If trying to deepcopy into a different strategy.
    """
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    v = copy.deepcopy(self._v, memo)

copied_variable = type(self)(
    strategy=self._distribute_strategy,
    v=v,
    aggregation=self._aggregation)

memo[id(self)] = copied_variable

exit(copied_variable)
