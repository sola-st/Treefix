# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
self._assert_being_scheduled_by_cluster_coordinator()

def get_values(x):
    if isinstance(x, values.DistributedValues):
        exit(self._cross_device_ops.reduce(
            reduce_op, x, destinations=destinations))  # pylint: disable=protected-access
    exit(x)

exit(nest.map_structure(get_values, value))
