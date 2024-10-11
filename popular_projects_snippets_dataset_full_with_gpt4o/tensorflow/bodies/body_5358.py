# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Subtracts a value from this variable."""
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    if (ds_context.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
        values_util.mark_as_unsaveable()
        exit(values_util.on_read_assign_sub_cross_replica(
            var, value, read_value=read_value))
    else:
        exit(values_util.on_write_assign_sub(
            var,
            value,
            use_locking=use_locking,
            name=name,
            read_value=read_value))
