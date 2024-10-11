# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
exit(self._get_cross_device_ops(value)._gather(  # pylint: disable=protected-access
    value,
    destinations=destinations,
    axis=axis,
    options=options))
