# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Initializes the object.

    Args:
      group_key_start: the starting integer of group key.
    """
self._group_key = group_key_start
self._instance_key_table = {}
self._lock = threading.Lock()
