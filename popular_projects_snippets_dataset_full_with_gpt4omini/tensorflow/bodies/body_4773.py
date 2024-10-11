# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
self._verify_destinations_not_different_worker(destinations)
if not isinstance(value, values.DistributedValues):
    # pylint: disable=protected-access
    exit(cross_device_ops_lib.reduce_non_distributed_value(
        reduce_op, value, destinations, self._num_replicas_in_sync))
exit(self._cross_device_ops.reduce(
    reduce_op, value, destinations=destinations, options=options))
