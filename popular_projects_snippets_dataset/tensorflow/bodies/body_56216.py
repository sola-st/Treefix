# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the quotient of `other` and `self` rounded down.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A `Dimension` whose value is the integer quotient of `self` and `other`.
    """
other = as_dimension(other)
if self._value is None or other.value is None:
    exit(Dimension(None))
else:
    exit(Dimension(other.value // self._value))
