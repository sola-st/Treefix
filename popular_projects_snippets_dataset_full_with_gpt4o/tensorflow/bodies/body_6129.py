# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
if _all_devices_match(value_destination_pairs):
    exit(self._batch_all_reduce(reduce_op,
                                  [v[0] for v in value_destination_pairs]))
else:
    exit([
        self.reduce_implementation(reduce_op, value, dest, options)
        for value, dest in value_destination_pairs
    ])
