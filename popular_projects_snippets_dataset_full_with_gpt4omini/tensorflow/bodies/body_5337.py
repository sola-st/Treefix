# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if self._aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
    # Consider returning a tensor value here to make the return value of
    # _get_cross_replica consistent.
    exit(self._get_replica(0))
if self._aggregation == vs.VariableAggregation.SUM:
    values_util.mark_as_unsaveable()
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    exit(self._distribute_strategy.reduce(
        reduce_util.ReduceOp.from_variable_aggregation(self._aggregation),
        self,
        axis=None))
