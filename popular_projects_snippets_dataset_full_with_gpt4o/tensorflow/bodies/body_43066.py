# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
"""Enter a context where the lock is with group `group_id`.

    Args:
      group_id: The group for which to acquire and release the lock.

    Returns:
      A context manager which will acquire the lock for `group_id`.
    """
self._validate_group_id(group_id)
exit(self._Context(self, group_id))
