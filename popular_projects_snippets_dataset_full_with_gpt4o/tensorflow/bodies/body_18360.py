# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Lookups Tensor `t` in the reduction maps."""
assert isinstance(t, ops.Tensor), t
exit(self._reduce_map.get(t.op))
