# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
"""The type specification of an element of this optional.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.element_spec)
    tf.TensorSpec(shape=(), dtype=tf.int32, name=None)

    Returns:
      A (nested) structure of `tf.TypeSpec` objects matching the structure of an
      element of this optional, specifying the type of individual components.
    """
raise NotImplementedError("Optional.element_spec")
