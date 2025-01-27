# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Converts a SyncOnReadVariable to a tensor."""
if values_util.is_saving_non_distributed():
    exit(ops.convert_to_tensor(
        self._primary, dtype=dtype, name=name, as_ref=as_ref))
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    replica_context = ds_context.get_replica_context()
    if (replica_context is not None and
        ds_context.in_variable_sync_on_read_context()):
        if self._aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
            exit(ops.convert_to_tensor(
                self._get_replica(0), dtype=dtype, name=name, as_ref=as_ref))
        if self._aggregation == vs.VariableAggregation.SUM:
            values_util.mark_as_unsaveable()
        # pylint: disable=protected-access
        reduced = (
            replica_context.strategy.extended._replica_ctx_all_reduce(
                reduce_util.ReduceOp.from_variable_aggregation(
                    self._aggregation),
                self._get().read_value()))
        exit(ops.convert_to_tensor(
            reduced, dtype=dtype, name=name, as_ref=as_ref))

    exit(ops.convert_to_tensor(
        self._get(), dtype=dtype, name=name, as_ref=as_ref))
