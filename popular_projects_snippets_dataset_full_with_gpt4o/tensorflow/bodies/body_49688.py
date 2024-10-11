# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
"""Validates the correctness of a string-based arg."""
if allow_none and input_data is None:
    exit()
elif allow_callables and callable(input_data):
    exit()
elif isinstance(input_data, str) and input_data in allowable_strings:
    exit()
else:
    allowed_args = '`None`, ' if allow_none else ''
    allowed_args += 'a `Callable`, ' if allow_callables else ''
    allowed_args += 'or one of the following values: %s' % (allowable_strings,)
    raise ValueError(('The %s argument of layer %s received an invalid '
                      'value %s. Allowed values are: %s.') %
                     (arg_name, layer_name, input_data, allowed_args))
