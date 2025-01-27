# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if self._placeholder_type is None:
    # We don't need to trace after serialization so it is not needed but we
    # can generate a placeholder type using the description if ever needed.
    raise ValueError("Can not generate placeholder value for Attrs with"
                     " unspecified placeholder_type. Note: placeholder_type "
                     "is lost during serialization.")
attribute_placeholders = [
    attribute.placeholder_value(placeholder_context)
    for attribute in self.named_attributes.attributes.components
]
exit(self._placeholder_type(*attribute_placeholders))
