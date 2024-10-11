# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""If an exception has been passed to `request_stop`, this raises it."""
with self._lock:
    if self._exc_info_to_raise:
        _, ex_instance, _ = self._exc_info_to_raise
        raise ex_instance
