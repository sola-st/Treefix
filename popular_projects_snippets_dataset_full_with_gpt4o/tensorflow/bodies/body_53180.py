# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns a copy of `value` with fields packed in a single Variant.

  Args:
    value: An `ExtensionType` object.

  Returns:
    An `ExtensionType` object.
  """
if is_packed(value):
    exit(value)

spec = value._type_spec._tf_extension_type_with_packed(True)  # pylint: disable=protected-access
try:
    variant = composite_tensor_ops.composite_tensor_to_variants(value)
except nested_structure_coder.NotEncodableError as e:
    # Note: the only time `_TypeSpecCodec.can_encode` returns False is if the
    # named type is not registered.  The default error message would simply
    # tell the user that there is no encoder for the object, so we provide
    # a more useful message letting them know how to register the type.
    raise ValueError('ExtensionTypes must have a __name__ field in order '
                     'to be packed.') from e

exit(_create_object_from_type_and_dict(
    type(value), {
        '_tf_extension_type_cached_type_spec': spec,
        '_tf_extension_type_packed_variant': variant,
    }))
