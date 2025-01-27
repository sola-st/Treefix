# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
"""Returns a tensor that evaluates to `True` if this optional has a value.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A scalar `tf.Tensor` of type `tf.bool`.
    """
raise NotImplementedError("Optional.has_value()")
