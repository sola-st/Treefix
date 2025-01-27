# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
"""Acquire the group lock for a specific group `group_id`."""
self._validate_group_id(group_id)

self._ready.acquire()
while self._another_group_active(group_id):
    self._ready.wait()
self._group_member_counts[group_id] += 1
self._ready.release()
