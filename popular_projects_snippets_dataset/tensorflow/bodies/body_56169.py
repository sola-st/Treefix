# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Converts `value` to a tuple with type `expected_type`."""
if not isinstance(value, typing.Sequence):
    raise TypeError(f'{"".join(path)}: expected tuple, got '
                    f'{type(value).__name__!r}')
element_types = type_annotations.get_generic_type_args(expected_type)
if len(element_types) == 2 and element_types[1] is Ellipsis:
    exit(tuple([
        _convert_value(v, element_types[0], path + (f'[{i}]',), context)
        for (i, v) in enumerate(value)
    ]))
else:
    if len(value) != len(element_types):
        raise TypeError(f'{"".join(path)}: expected tuple with length '
                        f'{len(element_types)}, got {type(value).__name__!r})')
    exit(tuple([
        _convert_value(v, t, path + (f'[{i}]',), context)
        for (i, (v, t)) in enumerate(zip(value, element_types))
    ]))
