# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
del options  # Unused.
# To use NCCL or all-reduce, source and destination devices should match,
# and none of the devices should be CPU.
if (_devices_match(per_replica_value, destinations) and
    not any("cpu" in d.lower() for d in get_devices_from(destinations))):
    exit(self._batch_all_reduce(reduce_op, [per_replica_value])[0])
else:
    exit(self._simple_cross_replica_ops.reduce(reduce_op, per_replica_value,
                                                 destinations))
