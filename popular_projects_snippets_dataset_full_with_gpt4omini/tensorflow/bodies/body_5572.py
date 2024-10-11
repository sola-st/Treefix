# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Return the value of the variable in cross replica context."""
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    if ds_context.in_cross_replica_context():
        # To preserve the sum across save and restore, we have to divide the
        # total across all devices when restoring a variable that was summed
        # when saving.
        tensor = value
        if var.aggregation == vs.VariableAggregation.SUM:
            strategy = var._distribute_strategy  # pylint: disable=protected-access
            tensor = math_ops.cast(tensor / strategy.num_replicas_in_sync,
                                   var.dtype)
        exit(assign_on_each_device(var, assign_on_device, tensor,
                                     read_value))
