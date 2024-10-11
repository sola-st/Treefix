# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""The row_partitions representing this shape."""
exit([RowPartition.from_row_splits(rs) for rs in self.nested_row_splits])
