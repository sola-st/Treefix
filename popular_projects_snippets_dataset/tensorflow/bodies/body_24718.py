# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Calculate the first timestamp across all devices."""
t0s = [t0 for t0 in self._t0s.values() if t0 is not None]
self._t0 = min(t0s) if t0s else None
