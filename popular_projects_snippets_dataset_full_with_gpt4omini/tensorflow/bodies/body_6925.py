# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
if input_workers is None:
    raise ValueError("`input_workers` should be "
                     "provided.")

error_message = ("Either `input_workers` or "
                 "both `components` and `element_spec` need to be "
                 "provided.")
self._options = options

if iterators is None:
    if (components is None or element_spec is None):
        raise ValueError(error_message)
    self._element_spec = element_spec
    self._input_workers = input_workers
    self._iterators = components
    self._strategy = strategy
    self._cardinality = cardinality
    self._enable_get_next_as_optional = enable_get_next_as_optional
else:
    if (components is not None and element_spec is not None):
        raise ValueError(error_message)

    super(DistributedIterator,
          self).__init__(input_workers, iterators, strategy, cardinality,
                         enable_get_next_as_optional)
