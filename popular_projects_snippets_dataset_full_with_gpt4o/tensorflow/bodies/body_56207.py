# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Raises an exception if `other` is not compatible with this Dimension.

    Args:
      other: Another Dimension.

    Raises:
      ValueError: If `self` and `other` are not compatible (see
        is_compatible_with).
    """
if not self.is_compatible_with(other):
    raise ValueError("Dimensions %s and %s are not compatible" %
                     (self, other))
