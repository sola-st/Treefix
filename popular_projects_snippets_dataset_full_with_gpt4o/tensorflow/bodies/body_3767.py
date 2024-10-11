# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
assert isinstance(value, collections.abc.Mapping)
flattened_values = []
for key in sorted(self.mapping.keys()):
    comp_value, comp_type = value[key], self.mapping[key]
    flattened_values.extend(comp_type._to_tensors(comp_value))  # pylint: disable=protected-access
exit(flattened_values)
