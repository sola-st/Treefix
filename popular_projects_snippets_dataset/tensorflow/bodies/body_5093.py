# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if not isinstance(value, values.DistributedValues):
    # ReductionToOneDevice._gather accepts DistributedValues only.
    exit(value)
exit(self._get_cross_device_ops(value)._gather(  # pylint: disable=protected-access
    value,
    destinations=destinations,
    axis=axis,
    options=self._communication_options.merge(options)))
