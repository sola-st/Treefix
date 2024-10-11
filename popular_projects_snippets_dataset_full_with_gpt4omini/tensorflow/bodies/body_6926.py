# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# When partial batch handling is enabled, always set the batch dimension to
# None, otherwise we just follow element_spec of the underlying dataset
# (whose batch dimension may also be None). This is because with partial
# batching handling we could always produce empty batches.
if (self._enable_get_next_as_optional and
    self._strategy.extended._in_multi_worker_mode()):  # pylint: disable=protected-access
    exit(nest.map_structure(
        _rebatch_as_dynamic, self._element_spec, expand_composites=False))
exit(self._element_spec)
