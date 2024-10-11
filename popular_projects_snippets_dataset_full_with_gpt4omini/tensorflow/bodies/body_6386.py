# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if (isinstance(value, values.Mirrored) and
    reduce_op == reduce_util.ReduceOp.MEAN):
    exit(value)
assert not isinstance(value, values.Mirrored)

if (isinstance(value, values.DistributedValues) and
    len(self.worker_devices) == 1):
    value = value.values[0]

# When there are multiple workers, we need to reduce across workers using
# collective ops.
if (not isinstance(value, values.DistributedValues) and
    self._num_workers == 1):
    # This function handles reducing values that are not PerReplica or
    # Mirrored values. For example, the same value could be present on all
    # replicas in which case `value` would be a single value or value could
    # be 0.
    exit(cross_device_ops_lib.reduce_non_distributed_value(
        reduce_op, value, destinations, len(self.worker_devices)))
exit(self._get_cross_device_ops(value).reduce(
    reduce_op,
    value,
    destinations=destinations,
    options=self._communication_options.merge(options)))
