# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
for _, destinations in value_destination_pairs:
    self._verify_destinations_not_different_worker(destinations)
exit(self._cross_device_ops.batch_reduce(reduce_op,
                                           value_destination_pairs, options))
