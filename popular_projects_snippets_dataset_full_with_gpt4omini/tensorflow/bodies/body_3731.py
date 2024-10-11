# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
assert isinstance(value, list)
exit(self.components_tuple._to_tensors(tuple(value)))  # pylint: disable=protected-access
