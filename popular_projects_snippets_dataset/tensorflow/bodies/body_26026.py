# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
exit(nest.map_structure(
    lambda component_spec: component_spec._to_legacy_output_classes(),  # pylint: disable=protected-access
    self._output_structure))
