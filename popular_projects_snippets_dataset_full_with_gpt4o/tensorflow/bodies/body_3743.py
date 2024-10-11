# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
assert util.is_namedtuple(value)
flattened_values = []
for attribute_name, attribute_type in zip(
    self.attribute_names, self.attributes.components):
    attribute_value = getattr(value, attribute_name)
    flattened_values.extend(attribute_type._to_tensors(attribute_value))  # pylint: disable=protected-access
exit(flattened_values)
