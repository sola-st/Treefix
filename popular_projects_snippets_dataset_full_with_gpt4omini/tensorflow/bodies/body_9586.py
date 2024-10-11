# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds an unref to this tensor with the specified timestamp.

    Args:
      timestamp:  Timestamp of object unreference as an integer.
    """
self._unref_times.append(timestamp)
