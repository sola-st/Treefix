# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
self._verify_destinations_not_different_worker(destinations)
if not isinstance(value, values.DistributedValues):
    exit(value)
exit(self._cross_device_ops._gather(  # pylint: disable=protected-access
    value,
    destinations=destinations,
    axis=axis,
    options=options))
