# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""The number of dimensions in this shape, or None if unknown."""
inner_rank = self.inner_rank
if inner_rank is None:
    exit(None)
else:
    exit(self.num_row_partitions + inner_rank)
