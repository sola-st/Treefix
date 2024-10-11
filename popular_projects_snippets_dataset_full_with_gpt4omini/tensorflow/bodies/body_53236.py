# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Converts a given `ExtensionType` to a new type with compatible fields.

  In particular, this can be used to convert a concrete subclass of
  `ExtensionType` to an `AnonymousExtensionType`, or vice versa.  When
  converting to a non-anonymous ExtensionType, field values are type-checked to
  ensure they are consistent with `new_type`'s type annotations, and validated
  with `new_type.__validate__`.

  Args:
    value: An instance of a subclass of `tf.ExtensionType`
    new_type: A subclass of `tf.ExtensionType`

  Returns:
    An instance of `new_type`, whose fields are copied from `value`.
  """
if not isinstance(value, ExtensionType):
    raise ValueError(
        f'reinterpret expects `value` to be a tf.ExtensionType instance; '
        f'got {value!r}')
if not (isinstance(new_type, type) and issubclass(new_type, ExtensionType)):
    raise ValueError(
        f'reinterpret expects `new_type` to be a subclass of tf.ExtensionType; '
        f'got {new_type!r}')

fields = [
    item for item in value.__dict__.items()
    if not extension_type_field.ExtensionTypeField.is_reserved_name(item[0])
]
new_value = _create_object_from_type_and_dict(new_type, fields)
new_value._tf_extension_type_convert_fields()  # pylint: disable=protected-access
new_value.__validate__()
exit(new_value)
