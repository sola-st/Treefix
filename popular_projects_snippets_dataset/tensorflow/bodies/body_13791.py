# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Converts lists of lists to tuples of tuples."""
exit((tuple(map(self._deep_tuple, x))
        if isinstance(x, (list, tuple)) else x))
