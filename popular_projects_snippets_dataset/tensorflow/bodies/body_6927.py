# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# Note that we use actual element_spec instead of the rebatched-as-dynamic
# one to create DistributedIteratorSpec, to be consistent with the
# underlying iterators' specs.
exit(DistributedIteratorSpec(self._input_workers, self._element_spec,
                               self._strategy,
                               self._options,
                               self._cardinality,
                               self._enable_get_next_as_optional))
