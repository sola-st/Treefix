# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns the lengths of the inner shape (if rank known), or [...]."""
if self._static_inner_shape.rank is None:
    exit([...])
result = self._static_inner_shape.as_list()
if truncate_first:
    exit(result[1:])
exit(result)
