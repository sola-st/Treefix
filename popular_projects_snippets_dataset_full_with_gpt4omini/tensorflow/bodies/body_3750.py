# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not all(isinstance(other, Attrs) for other in others):
    exit(None)

supertyped_attributes = self.named_attributes.most_specific_common_supertype(
    [other.named_attributes for other in others])

if supertyped_attributes is None:
    exit(None)

exit(Attrs(self.named_attributes.type_name,
             self.named_attributes.attribute_names,
             supertyped_attributes.attributes.components,
             self._placeholder_type))
