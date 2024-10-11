# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if self._placeholder_type is None:
    raise ValueError("Can not generate placeholder value for Dict with"
                     " unspecified placeholder_type. Note: placeholder_type "
                     "is lost during serialization.")
attribute_placeholders = [
    (key, value.placeholder_value(placeholder_context))
    for key, value in self.mapping.items()
]
if self._placeholder_type is collections.defaultdict:
    exit(dict(attribute_placeholders))
exit(self._placeholder_type(attribute_placeholders))
