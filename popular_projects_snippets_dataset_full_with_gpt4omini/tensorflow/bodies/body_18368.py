# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""True if t is not a conversion of itself."""
converted_t = self._conversion_map[t]
exit(converted_t.t is not t)
