# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Checks that `value_type` contains only supported type annotations.

  Args:
    value_type: The type annotation to check.
    in_mapping_key: True if `value_type` is nested in the key of a mapping.
    allow_forward_references: If false, then raise an exception if a
      `value_type` contains a forward reference (i.e., a string literal).

  Raises:
    TypeError: If `value_type` contains an unsupported type annotation.
  """
if isinstance(value_type, str) or type_annotations.is_forward_ref(value_type):
    if allow_forward_references:
        exit()
    else:
        raise TypeError(f'Unresolved forward reference {value_type!r}')

if value_type in (int, float, str, bytes, bool, None, _NoneType,
                  dtypes.DType):
    exit()
elif (value_type in (ops.Tensor, tensor_shape.TensorShape) or
      (isinstance(value_type, type) and
       issubclass(value_type, composite_tensor.CompositeTensor))):
    if in_mapping_key:
        raise TypeError(f'Mapping had a key {value_type.__name__!r} with type '
                        f'{type(value_type).__name__!r}')
elif (type_annotations.is_generic_tuple(value_type) or
      type_annotations.is_generic_union(value_type)):
    type_args = type_annotations.get_generic_type_args(value_type)
    if (len(type_args) == 2 and type_args[1] is Ellipsis and
        type_annotations.is_generic_tuple(value_type)):  # `Tuple[X, ...]`
        validate_field_value_type(type_args[0], in_mapping_key,
                                  allow_forward_references)
    else:
        for arg in type_annotations.get_generic_type_args(value_type):
            validate_field_value_type(arg, in_mapping_key, allow_forward_references)
elif type_annotations.is_generic_mapping(value_type):
    key_type, value_type = type_annotations.get_generic_type_args(value_type)
    validate_field_value_type(key_type, True, allow_forward_references)
    validate_field_value_type(value_type, in_mapping_key,
                              allow_forward_references)
elif isinstance(value_type, type):
    raise TypeError(f'Unsupported type annotation {value_type.__name__!r}')
else:
    raise TypeError(f'Unsupported type annotation {value_type!r}')
