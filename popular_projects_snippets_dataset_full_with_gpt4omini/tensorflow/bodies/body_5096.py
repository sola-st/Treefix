# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
cross_device_ops = None
for value, _ in value_destination_pairs:
    if cross_device_ops is None:
        cross_device_ops = self._get_cross_device_ops(value)
    elif cross_device_ops is not self._get_cross_device_ops(value):
        raise ValueError("Inputs to batch_reduce_to must be either all on "
                         "the host or all on the compute devices.")
exit(cross_device_ops.batch_reduce(
    reduce_op,
    value_destination_pairs,
    options=self._communication_options.merge(options)))
