# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    if (ds_context.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
        if self._aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
            exit(var._get_replica(0).value())  # pylint: disable=protected-access
        exit(var._get_cross_replica())  # pylint: disable=protected-access
    else:
        exit(var._get_on_device_or_primary().value())  # pylint: disable=protected-access
