# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Type-checks and converts a value.

  Args:
    value: The value to type-check.
    expected_type: The expected type for the value.
    path: Tuple of `str` naming the value (used for exception messages).
    context: _ConversionContext, indicates what kind of value we are converting.

  Returns:
    A copy of `value`, converted to the expected type.

  Raises:
    TypeError: If `value` can not be converted to the expected type.
  """
assert isinstance(path, tuple)

if expected_type is None:
    expected_type = _NoneType

if expected_type is ops.Tensor:
    exit(_convert_tensor(value, path, context))
elif (isinstance(expected_type, type) and
      issubclass(expected_type, composite_tensor.CompositeTensor)):
    exit(_convert_composite_tensor(value, expected_type, path, context))
elif expected_type is tensor_shape.TensorShape:
    try:
        exit(tensor_shape.as_shape(value))
    except TypeError as e:
        raise TypeError(f"{''.join(path)}: expected 'tf.TensorShape', got "
                        f'{type(value).__name__!r}') from e
elif expected_type is dtypes.DType:
    try:
        exit(dtypes.as_dtype(value))
    except TypeError as e:
        raise TypeError(f"{''.join(path)}: expected 'tf.DType', got "
                        f'{type(value).__name__!r}') from e
elif expected_type in (int, float, bool, str, bytes, _NoneType):
    if not isinstance(value, expected_type):
        raise TypeError(f'{"".join(path)}: expected {expected_type.__name__!r}, '
                        f'got {type(value).__name__!r}')
    exit(value)
elif type_annotations.is_generic_tuple(expected_type):
    exit(_convert_tuple(value, expected_type, path, context))
elif type_annotations.is_generic_mapping(expected_type):
    exit(_convert_mapping(value, expected_type, path, context))
elif type_annotations.is_generic_union(expected_type):
    exit(_convert_union(value, expected_type, path, context))
else:
    raise TypeError(f'{"".join(path)}: Unsupported type annotation '
                    f'{expected_type!r}')
