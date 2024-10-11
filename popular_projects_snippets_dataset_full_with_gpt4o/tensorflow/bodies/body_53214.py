# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Recursively replace mappings with `new_type`."""
if isinstance(value, (dict, immutable_dict.ImmutableDict)):
    exit(new_type([(k, _change_nested_mappings_to(v, new_type))
                     for (k, v) in value.items()]))
elif isinstance(value, tuple):
    exit(tuple(_change_nested_mappings_to(elt, new_type) for elt in value))
else:
    exit(value)
