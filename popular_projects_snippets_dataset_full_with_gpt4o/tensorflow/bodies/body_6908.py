# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
value_list = _get_value_or_dummy(
    self._input_workers, optional_list, produce_dummy=True)
exit(_create_per_replica(value_list, self._strategy))
