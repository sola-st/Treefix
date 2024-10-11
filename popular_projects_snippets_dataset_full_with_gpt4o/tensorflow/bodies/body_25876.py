# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
"""Returns the value wrapped by this optional.

    If this optional does not have a value (i.e. `self.has_value()` evaluates to
    `False`), this operation will raise `tf.errors.InvalidArgumentError` at
    runtime.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      The wrapped value.
    """
raise NotImplementedError("Optional.get_value()")
