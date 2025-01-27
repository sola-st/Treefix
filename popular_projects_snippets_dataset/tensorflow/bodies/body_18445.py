# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Flattens a rank 2 tensor, adding an offset to each row."""
# Note that if `ids` is rank 1, it is broadcast to rank 2.
offset_delta = math_ops.cast(offset_delta, ids.dtype)
n = math_ops.cast(num_rows, dtype=ids.dtype)
offsets = math_ops.range(
    start=0, limit=n * offset_delta, delta=offset_delta, dtype=ids.dtype)
offsets = array_ops.expand_dims(offsets, -1)
ids += offsets
exit(array_ops.reshape(ids, [-1]))
