# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
"""Returns a `tf.experimental.Optional` that wraps the given value.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)

    Args:
      value: A value to wrap. The value must be convertible to `tf.Tensor` or
        `tf.CompositeTensor`.

    Returns:
      A `tf.experimental.Optional` that wraps `value`.
    """
with ops.name_scope("optional") as scope:
    with ops.name_scope("value"):
        element_spec = structure.type_spec_from_value(value)
        encoded_value = structure.to_tensor_list(element_spec, value)

exit(_OptionalImpl(
    gen_optional_ops.optional_from_value(encoded_value, name=scope),
    element_spec,
))
