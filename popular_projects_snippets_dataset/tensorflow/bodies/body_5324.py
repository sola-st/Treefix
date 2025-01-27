# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.assign_sub(value, use_locking, name, read_value))
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    if (ds_context.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
        values_util.mark_as_unsaveable()
        exit(values_util.on_read_assign_sub_cross_replica(
            self, value, read_value=read_value))
    else:
        exit(super(SyncOnReadVariable,
                     self).assign_sub(value, use_locking, name, read_value))
