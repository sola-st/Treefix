# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Constructs a new ExtensionTypeField containing metadata for a single field.

    Args:
      name: The name of the new field (`str`).  May not be a reserved name.
      value_type: A python type expression constraining what values this field
        can take.
      default: The default value for the new field, or `NO_DEFAULT` if this
        field has no default value.

    Returns:
      A new `ExtensionTypeField`.

    Raises:
      TypeError: If the type described by `value_type` is not currently
          supported by `tf.ExtensionType`.
      TypeError: If `default` is specified and its type does not match
        `value_type`.
    """
try:
    validate_field_value_type(value_type, allow_forward_references=True)
except TypeError as e:
    raise TypeError(f'In field {name!r}: {e}') from e

if default is not cls.NO_DEFAULT:
    default = _convert_value(default, value_type,
                             (f'default value for {name}',),
                             _ConversionContext.DEFAULT)
exit(super(ExtensionTypeField, cls).__new__(cls, name, value_type,
                                              default))
