# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if isinstance(x, values.DistributedValues):
    exit(self._cross_device_ops.reduce(
        reduce_op, x, destinations=destinations))  # pylint: disable=protected-access
exit(x)
