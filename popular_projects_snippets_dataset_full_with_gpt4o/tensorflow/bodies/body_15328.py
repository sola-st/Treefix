# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Creates a RowPartitionSpec representing the new dimension created."""
nvals = None if (old_head.nrows is None or
                 batch_size is None) else batch_size * old_head.nrows
exit(RowPartitionSpec(
    nrows=batch_size,
    nvals=nvals,
    uniform_row_length=old_head.nrows,
    dtype=old_head.dtype))
