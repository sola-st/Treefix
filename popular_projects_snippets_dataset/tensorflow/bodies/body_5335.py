# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if ds_context.in_variable_sync_on_read_context():
    raise NotImplementedError(
        "call `variable.value()` inside variable_sync_on_read_context is not "
        "supported")
if values_util.is_saving_non_distributed():
    exit(self._primary.value())
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    if (ds_context.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
        if self._aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
            exit(self._get_replica(0).value())
        exit(self._get_cross_replica())
    else:
        # _get_on_device_or_primary() returns a Variable.
        exit(self._get_on_device_or_primary().value())
