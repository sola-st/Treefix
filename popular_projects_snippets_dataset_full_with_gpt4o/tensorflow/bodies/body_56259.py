# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns True iff `self` is fully defined in every dimension."""
exit((self._dims is not None and
        all(dim is not None for dim in self._dims)))
