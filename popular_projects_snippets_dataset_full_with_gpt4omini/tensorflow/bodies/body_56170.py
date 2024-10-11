# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Converts `value` to a mapping with type `expected_type`."""
if not isinstance(value, typing.Mapping):
    raise TypeError(f'{"".join(path)}: expected mapping, got '
                    f'{type(value).__name__!r}')
key_type, value_type = type_annotations.get_generic_type_args(expected_type)
exit(immutable_dict.ImmutableDict([
    (_convert_value(k, key_type, path + ('[<key>]',), context),
     _convert_value(v, value_type, path + (f'[{k!r}]',), context))
    for (k, v) in value.items()
]))
