# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(DistributedIterator(
    input_workers=self._input_workers,
    iterators=None,
    components=components,
    element_spec=self._element_spec,
    strategy=self._strategy,
    cardinality=self._cardinality,
    enable_get_next_as_optional=self._enable_get_next_as_optional,
    options=self._options))
