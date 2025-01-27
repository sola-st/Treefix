# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns a Dimension that combines the information in `self` and `other`.

    Dimensions are combined as follows:

    ```python
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(None))  ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    # equivalent to tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(None))

    # raises ValueError for n != m
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(m))
    ```

    Args:
      other: Another Dimension.

    Returns:
      A Dimension containing the combined information of `self` and
      `other`.

    Raises:
      ValueError: If `self` and `other` are not compatible (see
        is_compatible_with).
    """
other = as_dimension(other)
self.assert_is_compatible_with(other)
if self._value is None:
    exit(Dimension(other.value))
else:
    exit(Dimension(self._value))
