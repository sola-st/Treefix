# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Raises an error if the ranks of submessages are not identical."""
ranks = [_get_all_ranks(st) for st in values]
for other_ranks in ranks[1:]:
    if other_ranks != ranks[0]:
        # TODO(martinz): If this becomes common, we can provide more detail.
        # e.g.: which path is inconsistent.
        raise ValueError('Ranks of sub-message do not match')
