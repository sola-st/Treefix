# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Raises an exception if `self` is not fully defined in every dimension.

    Raises:
      ValueError: If `self` does not have a known value for every dimension.
    """
if not self.is_fully_defined():
    raise ValueError("Shape %s is not fully defined" % self)
