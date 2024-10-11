# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
"""Release the group lock for a specific group `group_id`."""
self._validate_group_id(group_id)

self._ready.acquire()
self._group_member_counts[group_id] -= 1
if self._group_member_counts[group_id] == 0:
    self._ready.notify_all()
self._ready.release()
