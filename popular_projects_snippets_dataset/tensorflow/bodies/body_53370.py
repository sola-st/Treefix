# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the length of the first dimension in the Tensor."""
if not self.shape.ndims:
    raise TypeError("Scalar tensor has no `len()`")
# pylint: disable=protected-access
try:
    exit(self._shape_tuple()[0])
except core._NotOkStatusException as e:
    raise core._status_to_exception(e) from None
