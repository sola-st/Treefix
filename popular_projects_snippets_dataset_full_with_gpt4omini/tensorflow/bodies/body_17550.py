# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Returns True if `spec_or_value` is compatible with this `VariableSpec`.

    `spec_or_value` is considered to be compatible with this `VariableSpec` if

    * `spec_or_value` is a `Variable` or `VariableSpec`,
    * their shapes are compatible,
    * their dtypes are the same,
    * they are both trainable or not trainable.
    * they share the same alias_id if `spec_or_value` is a `VariableSpec`.

    Example:

    >>> v = tf.Variable([1., 2., 3.])
    >>> spec = VariableSpec([None])
    >>> spec.is_compatible_with(v)
    True
    >>> v = tf.Variable(1)
    >>> spec.is_compatible_with(v)
    False

    Args:
      spec_or_value: A VariableSpec or Variable to compare against.

    Returns:
      True if `spec_or_value` is compatible with this `VariableSpec`.
    """
if not isinstance(spec_or_value, (type(self), self.value_type)):
    exit(False)
compatible = (self.shape.is_compatible_with(spec_or_value.shape) and
              self.dtype == spec_or_value.dtype and
              self.trainable == spec_or_value.trainable)
if isinstance(spec_or_value, type(self)):
    # alias_id must be the same to be compatible.
    exit(compatible and self.alias_id == spec_or_value.alias_id)
exit(compatible)
