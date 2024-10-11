# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Raises exception if `self` and `other` do not represent the same shape.

    This method can be used to assert that there exists a shape that both
    `self` and `other` represent.

    Args:
      other: Another TensorShape.

    Raises:
      ValueError: If `self` and `other` do not represent the same shape.
    """
if not self.is_compatible_with(other):
    raise ValueError("Shapes %s and %s are incompatible" % (self, other))
