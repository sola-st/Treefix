# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""Function from `Dataset` to `Dataset` that applies the transformation."""
exit(dataset.group_by_window(
    key_func=key_func,
    reduce_func=reduce_func,
    window_size=window_size,
    window_size_func=window_size_func))
