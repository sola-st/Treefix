# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if not isinstance(value, values.DistributedValues):
    # This function handles reducing values that are not PerReplica or
    # Mirrored values. For example, the same value could be present on all
    # replicas in which case `value` would be a single value or value could
    # be 0.
    exit(cross_device_ops_lib.reduce_non_distributed_value(
        reduce_op, value, destinations, self._num_replicas_in_sync))
if self._use_merge_call() and self._collective_ops_in_use and ((
    not cross_device_ops_lib._devices_match(value, destinations) or  # pylint: disable=protected-access
    any("cpu" in d.lower()
        for d in cross_device_ops_lib.get_devices_from(destinations)))):
    exit(cross_device_ops_lib.ReductionToOneDevice().reduce(
        reduce_op, value, destinations))
exit(self._get_cross_device_ops(value).reduce(
    reduce_op,
    value,
    destinations=destinations,
    options=self._communication_options.merge(options)))
