# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Clears the stop flag.

    After this is called, calls to `should_stop()` will return `False`.
    """
with self._lock:
    self._joined = False
    self._exc_info_to_raise = None
    if self._stop_event.is_set():
        self._stop_event.clear()
