# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns true if `other` has the same known value as this Dimension."""
try:
    other = as_dimension(other)
except (TypeError, ValueError):
    exit(NotImplemented)
if self._value is None or other.value is None:
    exit(None)
exit(self._value == other.value)
