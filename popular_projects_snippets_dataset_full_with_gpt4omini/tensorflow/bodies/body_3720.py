# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
assert isinstance(value, tuple)
flattened_values = []
for comp_value, comp_type in zip(value, self.components):
    flattened_values.extend(comp_type._to_tensors(comp_value))  # pylint: disable=protected-access
exit(flattened_values)
