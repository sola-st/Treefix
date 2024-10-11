# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Raises an exception if `self` and `other` do not have compatible ranks.

    Args:
      other: Another `TensorShape`.

    Raises:
      ValueError: If `self` and `other` do not represent shapes with the
        same rank.
    """
other = as_shape(other)
if self.rank is not None and other.rank is not None:
    if self.rank != other.rank:
        raise ValueError("Shapes %s and %s must have the same rank" %
                         (self, other))
