# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# We don't want to allow deserialization of this class because we don't
# serialize the strategy object. Currently the only places where
# _deserialize is called is when we save/restore using SavedModels.
if isinstance(input_workers, tuple):
    raise NotImplementedError("DistributedIteratorSpec does not have support "
                              "for deserialization.")
else:
    self._input_workers = input_workers
    self._element_spec = element_spec
    self._strategy = strategy
    self._cardinality = cardinality
    self._enable_get_next_as_optional = enable_get_next_as_optional
    self._options = options
    if self._strategy:
        self._canonicalize_devices = getattr(self._strategy,
                                             "_canonicalize_devices", True)
    else:
        self._canonicalize_devices = True
