# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Perform a deepcopy of the `DistributedVariable`.

    Unlike the deepcopy of a regular tf.Variable, this keeps the original
    strategy and devices of the `DistributedVariable`.  To avoid confusion
    with the behavior of deepcopy on a regular `Variable` (which does
    copy into new devices), we only allow a deepcopy of a `DistributedVariable`
    within its originating strategy scope.

    Args:
      memo: The memoization object for `deepcopy`.

    Returns:
      A deep copy of the current `DistributedVariable`.

    Raises:
      RuntimeError: If trying to deepcopy into a different strategy.
    """
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    new_values = []

    for value in self._values:
        with ops.device(value.device):
            new_values.append(copy.deepcopy(value, memo))

copied_variable = type(self)(
    strategy=self._distribute_strategy,
    values=new_values,
    aggregation=self._aggregation,
    var_policy=copy.deepcopy(self._policy, memo))

memo[id(self)] = copied_variable

exit(copied_variable)
