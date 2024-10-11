# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if self._aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
    exit(var._get_replica(0))  # pylint: disable=protected-access
if self._aggregation == vs.VariableAggregation.SUM:
    values_util.mark_as_unsaveable()
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    exit(var.distribute_strategy.reduce(
        reduce_util.ReduceOp.from_variable_aggregation(self._aggregation),
        var,
        axis=None))
