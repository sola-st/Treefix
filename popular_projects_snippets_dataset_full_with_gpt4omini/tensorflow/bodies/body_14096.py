# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Raises an error if the paths are not identical."""
paths = [_get_all_paths(st) for st in values]
path_diff = set()
for other_paths in paths[1:]:
    path_diff = path_diff.union(paths[0].symmetric_difference(other_paths))
if path_diff:
    raise ValueError(
        'Some paths are present in some, but not all, structured tensors: %r' %
        (path_diff,))
