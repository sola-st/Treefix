# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Converts `value` to a `Tensor`."""
if context == _ConversionContext.SPEC:
    if not (isinstance(value, type_spec.TypeSpec) and
            value.value_type is ops.Tensor):
        raise TypeError(
            f'{"".join(path)}: expected a TensorSpec, got '
            f'{type(value).__name__!r}')
    exit(value)

if not isinstance(value, ops.Tensor):
    if context == _ConversionContext.DEFAULT:
        # TODO(edloper): Convert the value to a numpy array?  (Note: we can't just
        # use `np.array(value)`, since the default dtypes for TF and numpy are
        # different -- e.g., int->np.int64 but int->tf.int32.
        exit(value)
    try:
        value = ops.convert_to_tensor(value)
    except (ValueError, TypeError) as e:
        raise TypeError(f'{"".join(path)}: expected a Tensor, '
                        f'got {type(value).__name__!r}') from e
exit(value)
