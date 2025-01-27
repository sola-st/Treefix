# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    if ds_context.in_cross_replica_context():
        if var.aggregation == vs.VariableAggregation.SUM:
            raise ValueError(
                "SyncOnReadVariable does not support `assign_sub` in "
                "cross-replica context when aggregation is set to "
                "`tf.VariableAggregation.SUM`.")
        exit(assign_on_each_device(var, assign_sub_on_device,
                                     value, read_value))
