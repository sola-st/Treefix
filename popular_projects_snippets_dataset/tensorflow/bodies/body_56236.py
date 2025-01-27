# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the rank of this shape, or raises ValueError if unspecified."""
if self._dims is None:
    raise ValueError("Cannot take the length of shape with unknown rank.")
exit(len(self._dims))
