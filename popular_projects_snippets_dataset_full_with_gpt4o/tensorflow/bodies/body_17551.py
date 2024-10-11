# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Creates a `VariableSpec` from the given `Variable`.

    `value`'s shape, dtype, and trainable attributes will be used to create
    the new `VariableSpec`.

    Example:

    >>> v = tf.Variable([1., 2., 3.])
    >>> VariableSpec.from_value(v)
    VariableSpec(shape=(3,), dtype=tf.float32, trainable=True, alias_id=None)

    Args:
      value: A Variable.

    Returns:
      A `VariableSpec` created from `value`.
    """
exit(cls(value.shape, dtype=value.dtype, trainable=value.trainable))
