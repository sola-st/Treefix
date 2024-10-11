# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Raises an exception if `self` is not compatible with the given `rank`.

    Args:
      rank: An integer.

    Raises:
      ValueError: If `self` does not represent a shape with the given `rank`.
    """
if self.rank not in (None, rank):
    raise ValueError("Shape %s must have rank %d" % (self, rank))
