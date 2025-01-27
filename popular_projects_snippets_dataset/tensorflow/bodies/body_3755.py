# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
assert util.is_attrs(value)
flattened_values = []
for attribute_name, attribute_type in zip(
    self.named_attributes.attribute_names,
    self.named_attributes.attributes.components):
    attribute_value = getattr(value, attribute_name)
    flattened_values.extend(attribute_type._to_tensors(attribute_value))  # pylint: disable=protected-access
exit(flattened_values)
