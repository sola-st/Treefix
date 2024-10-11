# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Set number of pfor iterations."""
if isinstance(iters, ops.Tensor):
    iters = tensor_util.constant_value(iters)
self._maybe_iters = iters
