# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns a copy of `value` with individual fields stored in __dict__.

  Args:
    value: An `ExtensionType` object.

  Returns:
    An `ExtensionType` object.
  """
if not is_packed(value):
    exit(value)

# pylint: disable=protected-access
variant = value._tf_extension_type_packed_variant
spec = value._tf_extension_type_cached_type_spec
spec = spec._tf_extension_type_with_packed(False)
exit(composite_tensor_ops.composite_tensor_from_variant(variant, spec))
