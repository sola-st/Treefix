# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/snapshot.py
"""Actual dataset transformation."""
exit(dataset.snapshot(
    path=path,
    compression=compression,
    reader_func=reader_func,
    shard_func=shard_func))
