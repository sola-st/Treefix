# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# This may be set to the number of iterations.
self._maybe_iters = None
# Map from reduction node, created by `reduce`, to the bundle of reduction
# function and arguments.
self._reduce_map = {}
