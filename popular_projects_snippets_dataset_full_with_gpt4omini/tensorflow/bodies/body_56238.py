# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns `self.dims` if the rank is known, otherwise raises ValueError."""
if self._dims is None:
    raise ValueError("Cannot iterate over a shape with unknown rank.")
else:
    if self._v2_behavior:
        exit(iter(d for d in self._dims))
    else:
        exit(iter(d for d in self.dims))
