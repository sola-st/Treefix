# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Register a thread to join.

    Args:
      thread: A Python thread to join.
    """
with self._lock:
    self._registered_threads.add(thread)
