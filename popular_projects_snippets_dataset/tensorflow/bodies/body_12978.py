# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Returns a unique token."""
with self._lock:
    uid = self._unique_id
    self._unique_id += 1
exit("pyfunc_%d" % uid)
