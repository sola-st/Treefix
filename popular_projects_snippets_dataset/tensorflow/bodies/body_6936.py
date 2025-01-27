# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(DistributedDataset(
    input_workers=self._input_workers,
    strategy=self._strategy,
    components=components,
    element_spec=self._element_spec,
    enable_get_next_as_optional=self._enable_get_next_as_optional,
    options=self._options))
