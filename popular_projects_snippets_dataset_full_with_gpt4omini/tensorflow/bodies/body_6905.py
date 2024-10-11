# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
value_list = _get_value_or_dummy(
    self._input_workers, optional_list, produce_dummy=True)
per_replica = _create_per_replica(value_list, self._strategy)
exit(optional_ops.Optional.from_value(per_replica))
