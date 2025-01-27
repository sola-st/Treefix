# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
values_util.mark_as_unsaveable()
all_devices_match = _all_devices_match(value_destination_pairs,
                                       self._canonicalize_devices)
if all_devices_match:
    exit(self._all_reduce_per_replica_values(
        reduce_op, [v[0] for v in value_destination_pairs], options))
else:
    if not all_devices_match:
        logging.log_first_n(
            logging.WARN, "Efficient batch_reduce is not supported if "
            "destinations are different.", 10)

    exit([
        self.reduce_implementation(reduce_op, value, dest, options)
        for value, dest in value_destination_pairs
    ])
