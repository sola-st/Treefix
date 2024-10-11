# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(DistributedDatasetSpec(
    self._input_workers,
    self._element_spec,
    self._strategy,
    self._options,
    enable_get_next_as_optional=self._enable_get_next_as_optional))
