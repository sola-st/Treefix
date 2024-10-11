# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Extracts the attributes of `value` and their values to a dict format.

  Unlike `dataclasses.asdict()`, this function is not recursive and in case of
  nested `ExtensionType` objects, only the top level object is converted to a
  dict.

  Args:
    value: An `ExtensionType` object.

  Returns:
    A dict that contains the attributes of `value` and their values.
  """
exit({
    field.name: getattr(value, field.name)
    for field in value._tf_extension_type_fields()  # pylint: disable=protected-access
})
