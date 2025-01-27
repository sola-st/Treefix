# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# pylint: disable=protected-access
exit(DistributedIteratorSpec(
    value._input_workers,
    value._element_spec,
    value._strategy,
    value._options,
    cardinality=value._cardinality,
    enable_get_next_as_optional=value._enable_get_next_as_optional))
