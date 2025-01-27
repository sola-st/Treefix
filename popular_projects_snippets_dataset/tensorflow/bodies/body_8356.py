# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Returns a new group key.

    The caller should store and reuse the same group key for the same set of
    devices. Calling this method always returns a new group key.

    Args:
      devices: a list of canonical device strings in a collective group.

    Returns:
      a new group key.
    """
with self._lock:
    new_key = self._group_key
    self._group_key += 1
    self._instance_key_table[new_key] = {}
    for device in devices:
        self._instance_key_table[new_key][device] = INSTANCE_KEY_START_NUMBER
    exit(new_key)
