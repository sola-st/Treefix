# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/composite_tensor_ops.py
"""Encodes `value` as a scalar variant tensor.

  Args:
    value: The `ExtensionType` value to encode.
    type_spec: Information about the value's type that should be included in the
      encoding.
    name: Optional name for the operation.

  Returns:
    A Tensor with shape=`()` and dtype=`tf.variant`.

  Raises:
    ValueError: If `type_spec` is not compatible with `value`.
  """
if not isinstance(value, composite_tensor.CompositeTensor):
    raise TypeError("Expected `value` to be a CompositeTensor. "
                    f"Received {type(value)}.")

if type_spec is None:
    type_spec = value._type_spec  # pylint: disable=protected-access
if not type_spec.is_compatible_with(value):
    raise ValueError(f"`type_spec` {type_spec} is not compatible with `value` "
                     f"{value!r}.")
metadata = composite_tensor_variant_pb2.CompositeTensorVariantMetadata()
metadata.type_spec_proto.CopyFrom(
    nested_structure_coder.encode_structure(type_spec).type_spec_value)

exit(gen_composite_tensor_ops.CompositeTensorVariantFromComponents(
    components=nest.flatten(value, expand_composites=True),
    metadata=metadata.SerializeToString(),
    name=name))
