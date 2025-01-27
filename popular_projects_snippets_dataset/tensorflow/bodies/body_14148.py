# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if callable(value):
    # `value` is actually a transforming function.
    if name not in new_fields:
        raise ValueError(
            '`StructuredTensor.with_updates` cannot update the field {} '
            'because a transforming function was given, but that field '
            'does not already exist.'.format(name_fullpath(name)))
    value = value(new_fields[name])
exit(value)
