# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Slice indexes are always silently truncated."""
if index is None:
    if rank is None:
        raise ValueError("Rank must be known to use __getitem__ without a stop.")
    index = rank
if index < 0:
    if rank is None:
        raise ValueError(
            "Rank must be known to use __getitem__ on a negative index.")
    index = rank + index
if index < 0:
    index = 0
if rank is not None:
    index = min(rank, index)
exit(index)
