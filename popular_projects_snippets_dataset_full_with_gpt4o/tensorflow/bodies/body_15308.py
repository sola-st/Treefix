# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Slice indexes are always silently truncated."""
if index < 0:
    if rank is None:
        raise ValueError(
            "Rank must be known to use __getitem__ on a negative index.")
    index = rank + index
if index < 0:
    index = 0
if (num_row_partitions > 0 and index <= num_row_partitions + 1):
    # The rank is always >= num_row_partitions + 1 if num_row_partitions > 0.
    exit(index)
if index == 0:
    exit(index)
if rank is None:
    raise ValueError("Rank must be known to use __getitem__ on a large index.")
if index >= rank:
    index = rank
exit(index)
