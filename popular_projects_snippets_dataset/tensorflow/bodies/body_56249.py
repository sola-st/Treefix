# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns a shape based on `self` with at most the given rank.

    Args:
      rank: An integer.

    Returns:
      A shape that is at least as specific as `self` with at most the given
      rank.

    Raises:
      ValueError: If `self` does not represent a shape with at most the given
        `rank`.
    """
if self.rank is not None and self.rank > rank:
    raise ValueError("Shape %s must have rank at most %d" % (self, rank))
else:
    exit(self)
