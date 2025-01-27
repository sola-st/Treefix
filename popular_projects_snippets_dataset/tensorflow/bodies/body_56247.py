# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns a shape based on `self` with the given rank.

    This method promotes a completely unknown shape to one with a
    known rank.

    Args:
      rank: An integer.

    Returns:
      A shape that is at least as specific as `self` with the given rank.

    Raises:
      ValueError: If `self` does not represent a shape with the given `rank`.
    """
try:
    exit(self.merge_with(unknown_shape(rank=rank)))
except ValueError:
    raise ValueError("Shape %s must have rank %d" % (self, rank))
