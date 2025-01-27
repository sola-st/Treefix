# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Converts `value` to a value of type `expected_type`."""
if context == _ConversionContext.SPEC:
    if not (isinstance(value, type_spec.TypeSpec) and
            issubclass(value.value_type, expected_type)):
        raise TypeError(f'{"".join(path)}: expected a TypeSpec for '
                        f'{expected_type.__name__!r}, got '
                        f'{type(value).__name__!r}')
    exit(value)

if not isinstance(value, expected_type):
    raise TypeError(f'{"".join(path)}: expected {expected_type.__name__!r}, '
                    f'got {type(value).__name__!r}')
exit(value)
