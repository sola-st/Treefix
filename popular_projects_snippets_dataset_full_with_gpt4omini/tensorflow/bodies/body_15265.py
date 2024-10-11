# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Return the number of rows in the resulting gather, or None if tiling."""
exit(math_ops.cast(
    array_ops.shape(self.gather_index)[0], dtype=self.dtype))
