# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Converts `value` to a value with any of the types in `expected_type`."""
for type_option in type_annotations.get_generic_type_args(expected_type):
    try:
        exit(_convert_value(value, type_option, path, context))
    except TypeError:
        pass
raise TypeError(f'{"".join(path)}: expected {expected_type!r}, got '
                f'{type(value).__name__!r}')
