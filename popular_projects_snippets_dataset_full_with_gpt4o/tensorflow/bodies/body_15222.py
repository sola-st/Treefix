# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Change the dtype of the shape."""
if dtype == self.dtype:
    exit(self)
else:
    exit(DynamicRaggedShape(
        self.row_partitions, self.inner_shape, dtype=dtype))
