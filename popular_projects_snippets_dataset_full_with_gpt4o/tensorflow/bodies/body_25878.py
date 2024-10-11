# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
"""Returns an `Optional` that has no value.

    NOTE: This method takes an argument that defines the structure of the value
    that would be contained in the returned `Optional` if it had a value.

    >>> optional = tf.experimental.Optional.empty(
    ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
    >>> print(optional.has_value())
    tf.Tensor(False, shape=(), dtype=bool)

    Args:
      element_spec: A (nested) structure of `tf.TypeSpec` objects matching the
        structure of an element of this optional.

    Returns:
      A `tf.experimental.Optional` with no value.
    """
exit(_OptionalImpl(gen_optional_ops.optional_none(), element_spec))
