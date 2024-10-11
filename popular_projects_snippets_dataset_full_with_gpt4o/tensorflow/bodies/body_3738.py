# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not all(
    isinstance(other, NamedTuple) and self.type_name == other.type_name and
    self.attribute_names == other.attribute_names for other in others):
    exit(None)

supertyped_attributes = self.attributes.most_specific_common_supertype(
    [other.attributes for other in others])

if supertyped_attributes is None:
    exit(None)

exit(NamedTuple(self.type_name, self.attribute_names,
                  supertyped_attributes.components, self._placeholder_type))
