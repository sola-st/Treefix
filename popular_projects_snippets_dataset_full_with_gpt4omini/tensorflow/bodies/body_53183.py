# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
# Use a tuple of (name, value) pairs, to ensure we preserve field ordering.
fields = [f.name for f in self._tf_extension_type_fields()]
if self._tf_extension_type_is_packed:
    fields.append('_tf_extension_type_is_packed')
exit(tuple(
    (f, _change_nested_mappings_to(self.__dict__[f], dict)) for f in fields))
