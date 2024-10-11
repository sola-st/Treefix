# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds a reference to this tensor with the specified timestamp.

    Args:
      timestamp:  Timestamp of object reference as an integer.
    """
self._ref_times.append(timestamp)
